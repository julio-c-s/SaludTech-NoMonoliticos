from datetime import datetime
from anonimizador.config.db import get_db
from anonimizador.modulos.anonimizador.dominio.entidades import ImagenAnonimizada
from anonimizador.modulos.anonimizador.infraestructura.repositorios import RepositorioImagenesSQL
from anonimizador.modulos.anonimizador.aplicacion.mapeadores import MapeadorImagenAnonimizadaDTOJson
from anonimizador.modulos.anonimizador.dominio.fabricas import FabricaImagenes
from anonimizador.modulos.anonimizador.dominio.eventos import (
    ImagenSubida, ImagenProcesada, ErrorProcesamientoImagen, ImagenEliminada
)
from anonimizador.modulos.anonimizador.infraestructura.event_dispatcher import dispatcher

class ServicioImagenAnonimizada:
    def __init__(self):
        self.session = get_db()
        self.repositorio = RepositorioImagenesSQL(self.session)
        self.mapeador = MapeadorImagenAnonimizadaDTOJson()
        self.fabrica = FabricaImagenes()

    def registrar_imagen(self, imagen_dto):
        imagen = self.fabrica.crear_objeto(imagen_dto, self.mapeador)
        if not hasattr(imagen, 'id'):
            raise AttributeError("El objeto ImagenAnonimizada debe contener un id")
        self.repositorio.guardar(imagen)
        evento = ImagenSubida(
            timestamp=datetime.now(),
            imagen_id=imagen.id,
            ruta_archivo=imagen.url_imagen_original
        )
        dispatcher.publicar(evento)
        return self.mapeador.entidad_a_dto(imagen)

    def obtener_imagen(self, id_imagen) -> ImagenAnonimizada:
        imagen = self.repositorio.obtener_por_id(id_imagen)
        if not imagen:
            raise ValueError(f"No se encontró la imagen con ID {id_imagen}")
        return imagen

    def obtener_todas_las_imagenes(self):
        imagenes = self.repositorio.obtener_todos()
        return [self.mapeador.entidad_a_dto(imagen) for imagen in imagenes]

    def actualizar_imagen(self, imagen_dto):
        try:
            imagen_existente = self.repositorio.obtener_por_id(imagen_dto.id)

            if not imagen_existente:
                raise ValueError(f"[ERROR] No se encontró la imagen con ID {imagen_dto.id}.")

            # Actualizar los campos
            imagen_existente.url_imagen_anonimizada = imagen_dto.url_imagen_anonimizada
            imagen_existente.estado_procesamiento = imagen_dto.estado_procesamiento

            print("Actualizando imagen en la base de datos...")  # Debugging
            self.repositorio.actualizar(imagen_existente)
            print("Imagen actualizada correctamente.")  # Debugging

            # Disparar evento
            evento = ImagenProcesada(
                timestamp=datetime.now(),
                imagen_id=imagen_existente.id,
                estado_procesamiento=imagen_existente.estado_procesamiento
            )
            dispatcher.publicar(evento)

            return self.mapeador.entidad_a_dto(imagen_existente)

        except Exception as e:
            print(f"Error al actualizar imagen: {str(e)}")  # Debugging
            raise e

    def eliminar_imagen(self, id_imagen):
        imagen = self.repositorio.obtener_por_id(id_imagen)
        if imagen:
            evento = ImagenEliminada(
                timestamp=datetime.now(),
                imagen_id=id_imagen,
                motivo="Eliminación solicitada"
            )
            dispatcher.publicar(evento)
        self.repositorio.eliminar(id_imagen)

    def obtener_por_id(self, id_imagen):
        try:
            return self.session.query(ImagenAnonimizada).filter(ImagenAnonimizada.id == str(id_imagen)).first()
        except Exception as e:
            print(f"Error obteniendo imagen por ID {id_imagen}: {str(e)}")
            return None
