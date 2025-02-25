# src/saludtech/modulos/procesador_imagenes/aplicacion/mapeadores.py

from saludtech.seedwork.aplicacion.dto import Mapeador as AppMap
from saludtech.modulos.procesador_imagenes.aplicacion.dto import ImagenMedicaDTO

class MapeadorImagenMedicaDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> ImagenMedicaDTO:
        """
        Convierte un diccionario (JSON) externo a una instancia de ImagenMedicaDTO.
        Se espera que el diccionario tenga las siguientes claves:
        - id
        - url
        - modalidad
        - region_anatomica
        - patologia
        - (opcional) estado_procesamiento
        """
        imagen_dto = ImagenMedicaDTO(
            id=externo.get("id"),
            url=externo.get("url"),
            modalidad=externo.get("modalidad"),
            region_anatomica=externo.get("region_anatomica"),
            patologia=externo.get("patologia"),
            estado_procesamiento=externo.get("estado_procesamiento", "pendiente")
        )
        return imagen_dto

    def dto_a_externo(self, dto: ImagenMedicaDTO) -> dict:
        """
        Convierte una instancia de ImagenMedicaDTO a un diccionario (JSON).
        """
        return {
            "id": dto.id,
            "url": dto.url,
            "modalidad": dto.modalidad,
            "region_anatomica": dto.region_anatomica,
            "patologia": dto.patologia,
            "estado_procesamiento": dto.estado_procesamiento
        }
