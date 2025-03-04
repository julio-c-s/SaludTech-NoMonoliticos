from saludtech.seedwork.dominio.entidades import Entidad  # Base class from seedwork
from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID, JSONB
from datetime import datetime
import uuid

class Notificacion(Entidad):
    __tablename__ = "notificaciones"

    _id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # Cambiado a _id
    mensaje = Column(String, nullable=False)
    destinatario = Column(String, nullable=False)
    estado_envio = Column(Enum("pendiente", "enviado", name="estado_envio_enum"), nullable=False, default="pendiente")
    fecha_creacion = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, id=None, mensaje=None, destinatario=None, estado_envio="pendiente"):
        super().__init__(id=id if id else uuid.uuid4())
        self.mensaje = mensaje
        self.destinatario = destinatario
        self.estado_envio = estado_envio

    def enviar_notificacion(self):
        # Lógica de dominio para enviar la notificación
        self.estado_envio = "enviado"

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id