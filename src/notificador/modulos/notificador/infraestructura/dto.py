from dataclasses import dataclass
from datetime import datetime

@dataclass
class NotificacionDTO:
    id: str
    mensaje: str
    destinatario: str
    estado_envio: str
    fecha_creacion: datetime