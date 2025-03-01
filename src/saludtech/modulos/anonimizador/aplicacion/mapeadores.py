import uuid
from saludtech.modulos.anonimizador.dominio.entidades import ImagenAnonimizada
from saludtech.modulos.anonimizador.dominio.objetos_valor import MetadatosClinicos

class MapeadorImagenAnonimizadaDTOJson:
    def obtener_tipo(self):
        return ImagenAnonimizada

    def dto_a_entidad(self, dto) -> ImagenAnonimizada:
        id_imagen = dto.get('id', str(uuid.uuid4()))  # Genera un UUID si 'id' no está presente
        return ImagenAnonimizada(id_imagen, dto['url_imagen_original'], dto.get('estado_procesamiento', 'pendiente'))

    def entidad_a_dto(self, entidad: ImagenAnonimizada) -> dict:
        return {
            'id': entidad.id,
            'id_imagen_original': entidad.id_imagen_original,
            'url_imagen_original': entidad.url_imagen_original,
            "url_imagen_anonimizada": entidad.url_imagen_anonimizada,
            "estado_procesamiento": entidad.estado_procesamiento
        }

    def externo_a_dto(self, externo: dict) -> ImagenAnonimizada:
        return self.dto_a_entidad(externo)
