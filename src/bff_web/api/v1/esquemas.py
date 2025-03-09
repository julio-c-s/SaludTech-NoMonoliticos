import strawberry
import datetime

@strawberry.type
class Imagen:
    id: str
    url: str
    modalidad: str
    region_anatomica: str
    patologia: str
    estado_procesamiento: str

@strawberry.type
class ImagenRespuesta:
    mensaje: str
    codigo: int
