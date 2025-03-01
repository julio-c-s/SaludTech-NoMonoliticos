from saludtech.modulos.anonimizador.dominio.entidades import ImagenAnonimizada 

def mapear_a_entidad(registro) -> ImagenAnonimizada:
    """
    Convierte un registro ORM a una instancia de ImagenAnonimizada.
    Se asume que 'registro' posee atributos: id, url, modalidad, region_anatomica, patologia y estado_procesamiento.
    """
    from saludtech.modulos.anonimizador.dominio.objetos_valor import MetadatosClinicos
    metadatos = MetadatosClinicos(registro.modalidad, registro.region_anatomica, registro.patologia)
    return ImagenAnonimizada(registro.id, registro.url, metadatos, registro.estado_procesamiento)

def mapear_a_registro(imagen: ImagenAnonimizada) -> dict:
    """
    Convierte una instancia de ImagenAnonimizada a un diccionario para persistencia.
    """
    return {
        "id": imagen.id,
        "id_imagen_original": imagen.metadatos.id_imagen_original,
        "url_imagen_original": imagen.url_imagen_original,
        "url_imagen_anonimizada": imagen.url_imagen_anonimizada,
        "estado_procesamiento": imagen.estado_procesamiento
    }