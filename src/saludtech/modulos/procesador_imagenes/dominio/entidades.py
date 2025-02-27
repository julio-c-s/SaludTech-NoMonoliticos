from saludtech.seedwork.dominio.entidades import Entidad  # Base class from seedwork
from saludtech.modulos.procesador_imagenes.dominio.objetos_valor import MetadatosClinicos
from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID, JSONB
from datetime import datetime
import uuid

class ImagenMedica(Entidad):
    __tablename__ = "imagenes_medicas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url = Column(String, nullable=False)
    metadatos = Column(JSONB, nullable=False)  # Se almacena como JSON en la DB
    estado_procesamiento = Column(Enum("pendiente", "procesado", name="estado_procesamiento_enum"), nullable=False, default="pendiente")
    fecha_creacion = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, id=None, url=None, metadatos=None, estado_procesamiento="pendiente"):
        super().__init__(id or uuid.uuid4())
        self.url = url
        self.metadatos = metadatos if metadatos else {}
        self.estado_procesamiento = estado_procesamiento

    def procesar_imagen(self):
        # Lógica de dominio para procesar la imagen
        self.estado_procesamiento = "procesado"