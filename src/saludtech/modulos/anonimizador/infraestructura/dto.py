# infraestructura/dto.py
from dataclasses import dataclass

@dataclass
class ImagenAnonimizadaDTO:
    id: str
    url: str
    modalidad: str
    region_anatomica: str
    patologia: str
    estado_procesamiento: str = "pendiente"
