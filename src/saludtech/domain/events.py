from dataclasses import dataclass

@dataclass
class DomainEvent:
    """Clase base para eventos de dominio."""
    pass

@dataclass
class ImageProcessedEvent(DomainEvent):
    """Evento de dominio que indica que una imagen ha sido procesada."""
    image_id: str
    diagnosis: dict
