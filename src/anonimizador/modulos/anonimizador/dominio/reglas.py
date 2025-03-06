class ReglaImagenUnica:
    """
    Regla para asegurar que no se registre una imagen con una URL duplicada.
    """
    def __init__(self, repositorio_imagenes):
        self.repositorio = repositorio_imagenes

    def es_valida(self, url: str) -> bool:
        imagen_existente = self.repositorio.obtener_por_url(url)
        return imagen_existente is None