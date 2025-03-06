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

class ServicioImagenMedica:
    def __init__(self):
        self.session = get_db()
        self.repositorio = RepositorioImagenesSQL(self.session)
        self.mapeador = MapeadorImagenMedicaDTOJson()
        self.fabrica = FabricaImagenes()
        # Inicializamos el cliente de Pulsar
        self.pulsar_client = PulsarClient()

    def registrar_imagen(self, imagen_dto):
        imagen = self.fabrica.crear_objeto(imagen_dto, self.mapeador)
        if not hasattr(imagen, 'id'):
            raise AttributeError("El objeto ImagenMedica debe contener un id")
        self.repositorio.guardar(imagen)
        evento = ImagenSubida(
            timestamp=datetime.now(),
            imagen_id=imagen.id,
            ruta_archivo=imagen.url
        )
        # Publicar el evento en el tópico "eventos.imagen" usando Pulsar
        self.pulsar_client.publish_event("eventos.imagen", asdict(evento))
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
