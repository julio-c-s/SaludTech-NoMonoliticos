from dataclasses import asdict
from infraestructura.pulsar_client import PulsarClient


class Despachador:
    def __init__(self):
        self.pulsar_client = PulsarClient()

    def publicar_evento(self, evento, topic: str):
        # Convierte el evento (usualmente una dataclass) a dict y lo publica
        self.pulsar_client.publish_event(topic, asdict(evento))