import uuid
from saludtech.modulos.anonimizador.dominio.entidades import ImagenAnonimizada

class MapeadorImagenAnonimizadaDTOJson:
    def obtener_tipo(self):
        return ImagenAnonimizada

    def dto_a_entidad(self, dto, entidad_existente=None) -> ImagenAnonimizada:
        id_imagen_original = dto.get('id_imagen_original', str(uuid.uuid4()))
        id_imagen = dto.get('id', id_imagen_original)
        
        # Mantener la URL de la imagen original si ya existe
        url_imagen_original = entidad_existente.url_imagen_original if entidad_existente else dto.get('url_imagen_original', '')

        return ImagenAnonimizada(id_imagen, url_imagen_original, dto.get('estado_procesamiento', 'pendiente'))


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
