import uuid
from saludtech.modulos.anonimizador.dominio.entidades import ImagenAnonimizada

class MapeadorImagenAnonimizadaDTOJson:
    def obtener_tipo(self):
        return ImagenAnonimizada

    def dto_a_entidad(self, dto, entidad_existente=None) -> ImagenAnonimizada:
        """
        Convierte un DTO en una entidad ImagenAnonimizada, asegurando que el ID y las URL no sean NULL.
        """
        if entidad_existente:
            id_imagen = entidad_existente.id
            url_imagen_original = entidad_existente.url_imagen_original
            url_imagen_anonimizada = entidad_existente.url_imagen_anonimizada  # Mantiene la URL ya almacenada
        else:
            id_imagen = dto.get('id')
            url_imagen_original = dto.get('url_imagen_original', '')
            url_imagen_anonimizada = dto.get('url_imagen_anonimizada', '')  # Si no se envía, usa un string vacío

        return ImagenAnonimizada(id_imagen, url_imagen_original, url_imagen_anonimizada, dto.get('estado_procesamiento', 'pendiente'))

    def entidad_a_dto(self, entidad: ImagenAnonimizada) -> dict:
        """
        Convierte una entidad ImagenAnonimizada en un diccionario para enviarlo en la respuesta.
        """

        return {
            'id': entidad.id,
            'id_imagen_original': entidad.id_imagen_original,
            'url_imagen_original': entidad.url_imagen_original,
            "url_imagen_anonimizada": entidad.url_imagen_anonimizada,
            "estado_procesamiento": entidad.estado_procesamiento
        }

    def externo_a_dto(self, externo: dict, entidad_existente=None) -> ImagenAnonimizada:
        imagen = self.dto_a_entidad(externo, entidad_existente)
        return imagen

