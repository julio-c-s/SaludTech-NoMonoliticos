from ..dominio.entidades import ImagenMedica

class MapeadorImagenMedicaDTOJson:
    def obtener_tipo(self):
        return ImagenMedica

    def dto_a_entidad(self, dto) -> ImagenMedica:
        from ..dominio.objetos_valor import MetadatosClinicos
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

def mapear_a_entidad(registro) -> ImagenMedica:
    """
    Convierte un registro ORM a una instancia de ImagenMedica.
    Se asume que 'registro' posee atributos: id, url, modalidad, region_anatomica, patologia y estado_procesamiento.
    """
    from ..dominio.objetos_valor import MetadatosClinicos
    metadatos = MetadatosClinicos(registro.modalidad, registro.region_anatomica, registro.patologia)
    return ImagenMedica(registro.id, registro.url, metadatos, registro.estado_procesamiento)

def mapear_a_registro(imagen: ImagenMedica) -> dict:
    """
    Convierte una instancia de ImagenMedica a un diccionario para persistencia.
    """
    return {
        "id": imagen.id,
        "url": imagen.url,
        "modalidad": imagen.metadatos.modalidad,
        "region_anatomica": imagen.metadatos.region_anatomica,
        "patologia": imagen.metadatos.patologia,
        "estado_procesamiento": imagen.estado_procesamiento
    }