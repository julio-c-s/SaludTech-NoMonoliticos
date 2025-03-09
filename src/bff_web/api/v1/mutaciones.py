import strawberry
from strawberry.types import Info
from saludtech.modulos.procesador.infraestructura.repositorios import RepositorioImagenesSQL
from saludtech.config.db import get_db
from saludtech.modulos.procesador.infraestructura.dto import ImagenMedicaDTO
from saludtech.modulos.procesador.infraestructura.pulsar_client import PulsarClient
from .esquemas import *

pulsar_client = PulsarClient()

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def registrar_imagen(self, id: str, url: str, modalidad: str, region_anatomica: str, patologia: str, info: Info) -> ImagenRespuesta:
        session = get_db()
        repo = RepositorioImagenesSQL(session)

        imagen_dto = ImagenMedicaDTO(id=id, url=url, modalidad=modalidad, region_anatomica=region_anatomica, patologia=patologia)
        repo.guardar(imagen_dto)

        evento = {
            "imagen_id": id,
            "ruta_archivo": url
        }
        pulsar_client.publish_event("eventos.imagen", evento)

        return ImagenRespuesta(mensaje="Imagen registrada y evento publicado", codigo=201)
