from dataclasses import dataclass, field
from uuid import uuid4

@dataclass
class Image:
    """
    Entidad de dominio que representa la imagen a procesar.
    """
    id: str = field(default_factory=lambda: str(uuid4()))
    status: str = "pending"   # pending, processing, processed, failed
    image_metadata: dict = field(default_factory=dict)
    diagnosis: dict = field(default_factory=dict)

    def mark_processing(self):
        self.status = "processing"

    def mark_processed(self, diagnosis: dict):
        self.status = "processed"
        self.diagnosis = diagnosis

    def mark_failed(self):
        self.status = "failed"
