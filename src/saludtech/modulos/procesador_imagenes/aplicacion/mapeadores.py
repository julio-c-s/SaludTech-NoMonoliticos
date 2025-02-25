from saludtech.modulos.procesador_imagenes.dominio.entidades import ImagenMedica
from saludtech.modulos.procesador_imagenes.dominio.objetos_valor import MetadatosClinicos


class MapeadorImagenMedicaDTOJson:
    def obtener_tipo(self):
        return ImagenMedica

    def dto_a_entidad(self, dto) -> ImagenMedica:
        metadatos = MetadatosClinicos(dto['modalidad'], dto['region_anatomica'], dto['patologia'])
        return ImagenMedica(dto['id'], dto['url'], metadatos, dto.get('estado_procesamiento', 'pendiente'))

    def entidad_a_dto(self, entidad: ImagenMedica) -> dict:
        return {
            "id": entidad.id,
            "url": entidad.url,
            "modalidad": entidad.metadatos.modalidad,
            "region_anatomica": entidad.metadatos.region_anatomica,
            "patologia": entidad.metadatos.patologia,
            "estado_procesamiento": entidad.estado_procesamiento
        }

    def externo_a_dto(self, externo: dict) -> ImagenMedica:
        return self.dto_a_entidad(externo)
