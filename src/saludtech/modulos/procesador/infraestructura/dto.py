# infraestructura/dto.py
from dataclasses import dataclass

@dataclass
class ImagenMedicaDTO:
    id: str
    url: str
    modalidad: str
    region_anatomica: str
    patologia: str
    estado_procesamiento: str = "pendiente"
