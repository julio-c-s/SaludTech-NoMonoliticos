# infraestructura/fabricas.py
from dataclasses import dataclass
from saludtech.modulos.anonimizador.dominio.entidades import ImagenAnonimizada
from saludtech.modulos.anonimizador.dominio.objetos_valor import MetadatosClinicos
from saludtech.config.db import get_db
from saludtech.seedwork.dominio.fabricas import Fabrica

class ImagenAnonimizadaFactory:
    @staticmethod
    def crear_imagen(id: str, url: str, modalidad: str, region_anatomica: str, patologia: str) -> ImagenAnonimizada:
        metadatos = MetadatosClinicos(modalidad, region_anatomica, patologia)
        return ImagenAnonimizada(id, url, metadatos)

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, clase_repositorio) -> any:
        # Obtain a DB session using your configuration helper.
        db_session = get_db()
        # Instantiate the repository class with the DB session.
        return clase_repositorio(db_session)