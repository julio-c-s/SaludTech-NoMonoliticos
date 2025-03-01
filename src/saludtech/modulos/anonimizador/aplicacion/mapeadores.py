import uuid
from saludtech.modulos.anonimizador.dominio.entidades import ImagenAnonimizada
from saludtech.modulos.anonimizador.dominio.objetos_valor import MetadatosClinicos

class MapeadorImagenAnonimizadaDTOJson:
    def obtener_tipo(self):
        return ImagenAnonimizada

    def dto_a_entidad(self, dto) -> ImagenAnonimizada:
        metadatos = MetadatosClinicos(dto.get('modalidad'), dto.get('region_anatomica'), dto.get('patologia'))
        id_imagen = dto.get('id', str(uuid.uuid4()))  # Genera un UUID si 'id' no está presente
        return ImagenAnonimizada(id_imagen, dto['url'], metadatos, dto.get('estado_procesamiento', 'pendiente'))

    def entidad_a_dto(self, entidad: ImagenAnonimizada) -> dict:
        return {
            "id": entidad.id,
            "url": entidad.url,
            "modalidad": entidad.metadatos.modalidad,
            "region_anatomica": entidad.metadatos.region_anatomica,
            "patologia": entidad.metadatos.patologia,
            "estado_procesamiento": entidad.estado_procesamiento
        }

    def externo_a_dto(self, externo: dict) -> ImagenAnonimizada:
        return self.dto_a_entidad(externo)
