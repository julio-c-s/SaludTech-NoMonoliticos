# infraestructura/fabricas.py
from dataclasses import dataclass
from saludtech.modulos.procesador.dominio.entidades import ImagenMedica
from saludtech.modulos.procesador.dominio.objetos_valor import MetadatosClinicos
from saludtech.config.db import get_db
from saludtech.seedwork.dominio.fabricas import Fabrica

class ImagenMedicaFactory:
    @staticmethod
    def crear_imagen(id: str, url: str, modalidad: str, region_anatomica: str, patologia: str) -> ImagenMedica:
        metadatos = MetadatosClinicos(modalidad, region_anatomica, patologia)
        return ImagenMedica(id, url, metadatos)

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, clase_repositorio) -> any:
        # Obtain a DB session using your configuration helper.
        db_session = get_db()
        # Instantiate the repository class with the DB session.
        return clase_repositorio(db_session)