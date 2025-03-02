import uuid
from saludtech.modulos.anonimizador.dominio.entidades import ImagenAnonimizada

class MapeadorImagenAnonimizadaDTOJson:
    def obtener_tipo(self):
        return ImagenAnonimizada

    def dto_a_entidad(self, dto, entidad_existente=None) -> ImagenAnonimizada:
        """
        Convierte un DTO en una entidad ImagenAnonimizada, asegurando que el ID no cambie si ya existe.
        """

        if entidad_existente:
            id_imagen = entidad_existente.id  # Mantiene el ID original si la imagen ya existe
            url_imagen_original = entidad_existente.url_imagen_original
        else:
            # Si no existe, usa el ID del DTO (si está presente) o lanza error
            id_imagen = dto.get('id')
            if not id_imagen:
                raise ValueError("[ERROR] Se esperaba un ID en la solicitud, pero no se encontró.")

            url_imagen_original = dto.get('url_imagen_original', '')

        print(f"[DEBUG] ID después del mapeo (verificar que no cambie): {id_imagen}")  

        return ImagenAnonimizada(id_imagen, url_imagen_original, dto.get('estado_procesamiento', 'pendiente'))


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
        """
        Convierte una solicitud externa en una entidad ImagenAnonimizada.
        """

        return self.dto_a_entidad(externo, entidad_existente)
