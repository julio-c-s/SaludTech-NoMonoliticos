from saludtech.seedwork.dominio.entidades import Entidad  # Base class from seedwork
from saludtech.modulos.anonimizador.dominio.objetos_valor import MetadatosClinicos
from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID, JSONB
from datetime import datetime
import uuid

class ImagenAnonimizada(Entidad):
    __tablename__ = "imagenes_anonimizadas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_imagen_original = Column(UUID(as_uuid=True), nullable=False)
    url_imagen_original = Column(String, nullable=False)
    url_imagen_anonimizada = Column(String, nullable=False)
    estado_procesamiento = Column(Enum("pendiente", "procesado", name="estado_procesamiento_enum"), nullable=False, default="pendiente")
    fecha_creacion = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, id_imagen_original=None, url_imagen_original=None, url_imagen_anonimizada=None, estado_procesamiento="pendiente"):
        super().__init__(str(uuid.uuid4())) 
        self.id_imagen_original = id_imagen_original
        self.url_imagen_original = url_imagen_original
        self.url_imagen_anonimizada = url_imagen_anonimizada
        self.estado_procesamiento = estado_procesamiento

    def anonimizar_imagen(self):
        # Lógica de dominio para anonimizar la imagen
        self.estado_procesamiento = "procesado"