from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ImagenMedicaModel(Base):
    __tablename__ = 'imagenes_medicas'

    id = Column(String, primary_key=True)
    url = Column(String, nullable=False)
    modalidad = Column(String, nullable=False)
    region_anatomica = Column(String, nullable=False)
    patologia = Column(String, nullable=False)
    estado_procesamiento = Column(String, nullable=False)

    def __init__(self, id, url, modalidad, region_anatomica, patologia, estado_procesamiento):
        self.id = id
        self.url = url
        self.modalidad = modalidad
        self.region_anatomica = region_anatomica
        self.patologia = patologia
        self.estado_procesamiento = estado_procesamiento