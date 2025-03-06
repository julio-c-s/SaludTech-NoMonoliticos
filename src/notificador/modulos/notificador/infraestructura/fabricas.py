from dataclasses import dataclass
from notificador.modulos.notificador.dominio.entidades import Notificacion
from notificador.config.db import get_db
from notificador.seedwork.dominio.fabricas import Fabrica

class NotificacionFactory:
    @staticmethod
    def crear_notificacion(id: str, mensaje: str, destinatario: str, estado_envio: str) -> Notificacion:
        return Notificacion(id, mensaje, destinatario, estado_envio)
    
@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, clase_repositorio) -> any:
        # Obtain a DB session using your configuration helper.
        db_session = get_db()
        # Instantiate the repository class with the DB session.
        return clase_repositorio(db_session)