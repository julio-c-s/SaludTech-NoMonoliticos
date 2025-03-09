import strawberry
from .esquemas import *
from saludtech.modulos.procesador.infraestructura.repositorios import RepositorioImagenesSQL
from saludtech.config.db import get_db

@strawberry.type
class Query:
    @strawberry.field
    def imagen(self, id: str) -> Imagen:
        session = get_db()
        repo = RepositorioImagenesSQL(session)
        return repo.obtener_por_id(id)

    @strawberry.field
    def imagenes(self) -> list[Imagen]:
        session = get_db()
        repo = RepositorioImagenesSQL(session)
        return repo.obtener_todos()
