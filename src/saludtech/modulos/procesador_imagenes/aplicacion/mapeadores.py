import uuid
from saludtech.modulos.procesador_imagenes.dominio.entidades import ImagenMedica
from saludtech.modulos.procesador_imagenes.dominio.objetos_valor import MetadatosClinicos

class MapeadorImagenMedicaDTOJson:
    def obtener_tipo(self):
        return ImagenMedica

    def dto_a_entidad(self, dto) -> ImagenMedica:
        metadatos = MetadatosClinicos(dto.get('modalidad'), dto.get('region_anatomica'), dto.get('patologia'))
        id_imagen = dto.get('id', str(uuid.uuid4()))  # Genera un UUID si 'id' no está presente
        return ImagenMedica(id_imagen, dto['url'], metadatos, dto.get('estado_procesamiento', 'pendiente'))

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
