from anonimizador.modulos.anonimizador.dominio.entidades import ImagenAnonimizada 

def mapear_a_entidad(registro) -> ImagenAnonimizada:
    """
    Convierte un registro ORM a una instancia de ImagenAnonimizada.
    Se asume que 'registro' posee atributos: id, url, modalidad, region_anatomica, patologia y estado_procesamiento.
    """

    return ImagenAnonimizada(registro.id, registro.id_imagen_original, registro.url_imagen_original)

def mapear_a_registro(imagen: ImagenAnonimizada) -> dict:
    """
    Convierte una instancia de ImagenAnonimizada a un diccionario para persistencia.
    """
    return {
        "id": imagen.id,
        "id_imagen_original": imagen.id_imagen_original,
        "url_imagen_original": imagen.url_imagen_original,
        "url_imagen_anonimizada": imagen.url_imagen_anonimizada,
        "estado_procesamiento": imagen.estado_procesamiento
    }