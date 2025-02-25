from saludtech.seedwork.dominio.entidades import Entidad  # Base class from seedwork
from saludtech.modulos.procesador_imagenes.dominio.objetos_valor import MetadatosClinicos


class ImagenMedica(Entidad):
    def __init__(self, id, url, metadatos: MetadatosClinicos, estado_procesamiento="pendiente"):
        super().__init__(id)
        self.url = url
        self.metadatos = metadatos
        self.estado_procesamiento = estado_procesamiento

    def procesar_imagen(self):
        # Lógica de dominio para procesar la imagen
        self.estado_procesamiento = "procesado"