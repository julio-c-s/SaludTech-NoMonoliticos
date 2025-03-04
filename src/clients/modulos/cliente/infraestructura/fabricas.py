from dataclasses import dataclass, field
from clients.seedwork.dominio.fabricas import Fabrica
from clients.seedwork.dominio.repositorios import Repositorio
from clients.modulos.vuelos.dominio.repositorios import RepositorioProveedores, RepositorioReservas
from .repositorios import RepositorioImagenesSQL
from clients.config.db import get_db

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        session = get_db()
        return RepositorioImagenesSQL(session)
