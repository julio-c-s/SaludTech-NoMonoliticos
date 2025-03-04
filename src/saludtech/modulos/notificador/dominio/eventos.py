from dataclasses import dataclass
from datetime import datetime

@dataclass
class EventoDominio:
    """Clase base para eventos de dominio."""
    timestamp: datetime

@dataclass
class NotificacionEnviada(EventoDominio):
    """Evento de dominio para notificación enviada."""
    id: str
    destinatario: str

@dataclass
class NotificacionFallida(EventoDominio):
    """Evento de dominio para notificación fallida."""
    id: str
    destinatario: str

@dataclass
class NotificacionEliminada(EventoDominio):
    """Evento de dominio para notificación eliminada."""
    id: str
    destinatario: str