# infraestructura/fabricas.py
from modulos.procesador_imagenes.dominio.entidades import ImagenMedica
from modulos.procesador_imagenes.dominio.objetos_valor import MetadatosClinicos

class ImagenMedicaFactory:
    @staticmethod
    def crear_imagen(id: str, url: str, modalidad: str, region_anatomica: str, patologia: str) -> ImagenMedica:
        metadatos = MetadatosClinicos(modalidad, region_anatomica, patologia)
        return ImagenMedica(id, url, metadatos)
