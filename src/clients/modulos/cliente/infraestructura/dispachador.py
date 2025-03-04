from dataclasses import asdict
from infraestructura.pulsar_client import PulsarClient


class Despachador:
    def __init__(self):
        self.pulsar_client = PulsarClient()

    def publicar_evento(self, evento, topic: str):
        # Convierte el evento a diccionario (si es una dataclass)
        self.pulsar_client.publish_event(topic, asdict(evento))
