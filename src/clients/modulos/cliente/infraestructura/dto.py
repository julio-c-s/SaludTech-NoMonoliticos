# infraestructura/dto.py
from dataclasses import dataclass

@dataclass
class ImagenAnonimizadaDTO:
    id: int
    id_imagen_original: int
    url_imagen_original: str
    url_imagen_anonimizada: str
    estado_procesamiento: str
