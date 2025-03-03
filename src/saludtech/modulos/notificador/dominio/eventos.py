from dataclasses import dataclass
from datetime import datetime

@dataclass
class EventoDominio:
    """Clase base para eventos de dominio."""
    timestamp: datetime

@dataclass
class NotificacionEnviada(EventoDominio):
    """Evento de dominio para notificación enviada."""
    id_notificacion: str
    destinatario: str

@dataclass
class NotificacionFallida(EventoDominio):
    """Evento de dominio para notificación fallida."""
    id_notificacion: str
    error: str

@dataclass
class NotificacionEliminada(EventoDominio):
    """Evento de dominio para notificación eliminada."""
    id_notificacion: str
    motivo: str
    destinatario: str