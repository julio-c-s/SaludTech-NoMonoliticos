from dataclasses import dataclass
from datetime import datetime

@dataclass
class EventoDominio:
    """Clase base para eventos de dominio."""
    timestamp: datetime

@dataclass
class ImagenSubida(EventoDominio):
    """Evento que representa cuando una imagen es subida al sistema."""
    imagen_id: str
    ruta_archivo: str

@dataclass
class ImagenProcesada(EventoDominio):
    """Evento que indica que una imagen fue procesada exitosamente."""
    imagen_id: str
    estado_procesamiento: str

@dataclass
class ErrorProcesamientoImagen(EventoDominio):
    """Evento que indica que hubo un error al procesar una imagen."""
    imagen_id: str
    mensaje_error: str

@dataclass
class ImagenEliminada(EventoDominio):
    """Evento que representa cuando una imagen ha sido eliminada del sistema."""
    imagen_id: str
    motivo: str

@dataclass
class ImagenRegistradaSaga:
    timestamp: datetime
    imagen_id: str
    ruta_archivo: str
    estado: str = "INICIADA"  # Estado inicial

@dataclass
class ImagenRegistroCompensado:
    timestamp: datetime
    imagen_id: str
    motivo: str
    estado: str = "COMPENSADA"  # Estado de compensación
