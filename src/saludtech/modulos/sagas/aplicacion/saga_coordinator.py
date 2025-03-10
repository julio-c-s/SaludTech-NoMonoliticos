from datetime import datetime
from dataclasses import asdict, dataclass
from saludtech.config.db import get_db
from saludtech.modulos.procesador.infraestructura.repositorios import RepositorioImagenesSQL
from saludtech.modulos.procesador.infraestructura.pulsar_client import PulsarClient

# Definición de eventos de Saga (actualizados con el campo 'estado')
@dataclass
class ImagenRegistradaSaga:
    timestamp: datetime
    imagen_id: str
    ruta_archivo: str
    estado: str = "Procesado"

@dataclass
class ImagenRegistroCompensado:
    timestamp: datetime
    imagen_id: str
    motivo: str
    estado: str = "COMPENSADA"

class SagaCoordinator:
    """
    Coordinador de Saga para el registro de imágenes.
    Se encarga de:
      - Iniciar la saga: guardar la imagen, publicar un evento de inicio y registrar el log.
      - Ejecutar la compensación en caso de fallo: eliminar la imagen, publicar el evento compensatorio y registrar el log.
    """
    def __init__(self):
        self.pulsar_client = PulsarClient()
        # Implementación simple del Saga Log (se puede persistir en BD en producción)
        self.saga_log = []

    def iniciar_saga_registro_imagen(self, imagen):
        repositorio = RepositorioImagenesSQL(get_db())
        repositorio.guardar(imagen)
        
        evento = ImagenRegistradaSaga(
            timestamp=datetime.now(),
            imagen_id=str(imagen.id),
            ruta_archivo=imagen.url
        )
        self.pulsar_client.publish_event("sagas.imagen", asdict(evento))
        self.saga_log.append(asdict(evento))
        return evento

    def compensar_registro_imagen(self, imagen_id, motivo):
        repositorio = RepositorioImagenesSQL(get_db())
        imagen = repositorio.obtener_por_id(imagen_id)
        if imagen:
            repositorio.eliminar(imagen_id)
        
        evento = ImagenRegistroCompensado(
            timestamp=datetime.now(),
            imagen_id=str(imagen_id),
            motivo=motivo
        )
        self.pulsar_client.publish_event("sagas.imagen", asdict(evento))
        self.saga_log.append(asdict(evento))
        return evento

    def obtener_saga_log(self):
        return self.saga_log
