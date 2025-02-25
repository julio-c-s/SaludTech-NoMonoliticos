from dataclasses import dataclass
from saludtech.config.db import get_db

@dataclass
class FabricaRepositorio:
    def crear_objeto(self, clase_repositorio) -> any:
        # Obtain a DB session using your configuration helper.
        db_session = get_db()
        # Instantiate the repository class with the DB session.
        return clase_repositorio(db_session)