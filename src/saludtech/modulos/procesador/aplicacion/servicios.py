from datetime import datetime
from dataclasses import asdict
from saludtech.config.db import get_db
from saludtech.modulos.procesador.infraestructura.repositorios import RepositorioImagenesSQL
from saludtech.modulos.procesador.aplicacion.mapeadores import MapeadorImagenMedicaDTOJson
from saludtech.modulos.procesador.dominio.fabricas import FabricaImagenes
from saludtech.modulos.procesador.dominio.eventos import (
    ImagenSubida, ImagenProcesada, ErrorProcesamientoImagen, ImagenEliminada
)
from saludtech.modulos.procesador.infraestructura.pulsar_client import PulsarClient
from saludtech.modulos.sagas.aplicacion.saga_coordinator import SagaCoordinator
from saludtech.modulos.sagas.aplicacion.global_vars import saga_coordinator_global 

class ServicioImagenMedica:
    def __init__(self):
        self.session = get_db()
        self.repositorio = RepositorioImagenesSQL(self.session)
        self.mapeador = MapeadorImagenMedicaDTOJson()
        self.fabrica = FabricaImagenes()
        self.pulsar_client = PulsarClient()
        # Utiliza la instancia global importada desde global_vars
        self.saga_coordinator = saga_coordinator_global
    
    def registrar_imagen(self, imagen_dto):
        imagen = self.fabrica.crear_objeto(imagen_dto, self.mapeador)
        if not hasattr(imagen, 'id'):
            raise AttributeError("El objeto ImagenMedica debe contener un id")
        
        # Inicia la saga de registro de imagen usando la instancia global
        evento_saga = self.saga_coordinator.iniciar_saga_registro_imagen(imagen)
        return self.mapeador.entidad_a_dto(imagen)
    
    def obtener_imagen_por_id(self, id_imagen):
        imagen = self.repositorio.obtener_por_id(id_imagen)
        if imagen is None:
            return None
        return self.mapeador.entidad_a_dto(imagen)
    
    def obtener_todas_las_imagenes(self):
        imagenes = self.repositorio.obtener_todos()
        return [self.mapeador.entidad_a_dto(imagen) for imagen in imagenes]
    
    def actualizar_imagen(self, imagen_dto):
        imagen = self.fabrica.crear_objeto(imagen_dto, self.mapeador)
        self.repositorio.actualizar(imagen)
        evento = ImagenProcesada(
            timestamp=datetime.now(),
            imagen_id=imagen.id,
            estado_procesamiento=imagen.estado_procesamiento
        )
        self.pulsar_client.publish_event("eventos.imagen", asdict(evento))
        return self.mapeador.entidad_a_dto(imagen)
    
    def eliminar_imagen(self, id_imagen):
        imagen = self.repositorio.obtener_por_id(id_imagen)
        if imagen:
            evento = ImagenEliminada(
                timestamp=datetime.now(),
                imagen_id=id_imagen,
                motivo="Eliminación solicitada"
            )
            self.pulsar_client.publish_event("eventos.imagen", asdict(evento))
        self.repositorio.eliminar(id_imagen)
