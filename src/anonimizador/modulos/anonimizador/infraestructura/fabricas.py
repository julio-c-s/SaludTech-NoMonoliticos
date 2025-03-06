# infraestructura/fabricas.py
from dataclasses import dataclass
from anonimizador.modulos.anonimizador.dominio.entidades import ImagenAnonimizada
from anonimizador.config.db import get_db
from anonimizador.seedwork.dominio.fabricas import Fabrica

class ImagenAnonimizadaFactory:
    @staticmethod
    def crear_imagen(id: str, id_imagen_original:str, url_imagen_original:str, url_imagen_anonimizada:str, estado_procesamiento:str) -> ImagenAnonimizada:
         return ImagenAnonimizada(id, id_imagen_original, url_imagen_original, url_imagen_anonimizada, estado_procesamiento)

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, clase_repositorio) -> any:
        # Obtain a DB session using your configuration helper.
        db_session = get_db()
        # Instantiate the repository class with the DB session.
        return clase_repositorio(db_session)