import uuid
from saludtech.modulos.anonimizador.dominio.entidades import ImagenAnonimizada

class MapeadorImagenAnonimizadaDTOJson:
    def obtener_tipo(self):
        return ImagenAnonimizada

    def dto_a_entidad(self, dto, entidad_existente=None) -> ImagenAnonimizada:
        """
        Convierte un DTO en una entidad ImagenAnonimizada.
        """
        if entidad_existente:
            id_imagen = entidad_existente.id
        else:
            id_imagen = dto.get('id', str(uuid.uuid4()))

        id_imagen_original = dto.get('id_imagen_original', entidad_existente.id_imagen_original if entidad_existente else None)
        url_imagen_original = dto.get('url_imagen_original', entidad_existente.url_imagen_original if entidad_existente else None)
        url_imagen_anonimizada = dto.get('url_imagen_anonimizada', entidad_existente.url_imagen_anonimizada if entidad_existente else '')

        if not id_imagen_original or not url_imagen_original:
            raise ValueError("id_imagen_original y url_imagen_original son obligatorios")

        # Validar y corregir el valor de estado_procesamiento
        estado_procesamiento = dto.get('estado_procesamiento', entidad_existente.estado_procesamiento if entidad_existente else 'pendiente')
        
        if estado_procesamiento == "procesada":
            estado_procesamiento = "procesado"  # Cambiar a valor válido en la base de datos

        return ImagenAnonimizada(
            id=id_imagen,
            id_imagen_original=id_imagen_original,
            url_imagen_original=url_imagen_original,
            url_imagen_anonimizada=url_imagen_anonimizada,
            estado_procesamiento=estado_procesamiento
        )


    def entidad_a_dto(self, entidad: ImagenAnonimizada) -> dict:
        """
        Convierte una entidad ImagenAnonimizada en un diccionario para enviarlo en la respuesta.
        """

        return {
            'id': str(entidad.id),
            'id_imagen_original': str(entidad.id_imagen_original),
            'url_imagen_original': entidad.url_imagen_original,
            "url_imagen_anonimizada": entidad.url_imagen_anonimizada if entidad.url_imagen_anonimizada else "",
            "estado_procesamiento": entidad.estado_procesamiento
        }

    def externo_a_dto(self, externo: dict, entidad_existente=None) -> ImagenAnonimizada:
        imagen = self.dto_a_entidad(externo, entidad_existente)
        return imagen

