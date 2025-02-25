from saludtech.modulos.procesador_imagenes.dominio.entidades import ImagenMedica 

def mapear_a_entidad(registro) -> ImagenMedica:
    """
    Convierte un registro ORM a una instancia de ImagenMedica.
    Se asume que 'registro' posee atributos: id, url, modalidad, region_anatomica, patologia y estado_procesamiento.
    """
    from saludtech.modulos.procesador_imagenes.dominio.objetos_valor import MetadatosClinicos
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
