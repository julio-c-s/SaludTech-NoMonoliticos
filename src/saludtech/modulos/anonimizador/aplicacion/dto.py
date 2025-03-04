class ImagenAnonimizadaDTO:
    def __init__(self, id=None, id_imagen_original=None, url_imagen_original=None, url_imagen_anonimizada=None, estado_procesamiento="pendiente"):
        self.id = id
        self.id_imagen_original = id_imagen_original
        self.url_imagen_original = url_imagen_original
        self.url_imagen_anonimizada = url_imagen_anonimizada
        self.estado_procesamiento = estado_procesamiento
        
