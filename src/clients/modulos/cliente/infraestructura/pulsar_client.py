import os
import json
import io
import pulsar
from fastavro import writer, parse_schema
from datetime import datetime

class PulsarClient:
    def __init__(self, service_url=None):
        # Lee la URL del broker desde una variable de entorno o usa el valor por defecto
        service_url = service_url or os.getenv("PULSAR_SERVICE_URL", "pulsar://localhost:6650")
        self.client = pulsar.Client(service_url)
        self.producers = {}
        # Construir la ruta absoluta al esquema Avro para el evento, por ejemplo "ReservaCreada"
        base_dir = os.path.dirname(__file__)
        schema_path = os.path.join(base_dir, "schemas", "reserva_creada.avsc")
        with open(schema_path, "r") as schema_file:
            self.avro_schema = parse_schema(json.load(schema_file))

    def get_producer(self, topic):
        if topic not in self.producers:
            self.producers[topic] = self.client.create_producer(topic)
        return self.producers[topic]

    def publish_event(self, topic: str, message: dict):
        # Asegurarse de que los campos de tipo datetime se conviertan a string (ISO)
        if "timestamp" in message and isinstance(message["timestamp"], datetime):
            message["timestamp"] = message["timestamp"].isoformat()
        # Añadir el versionado básico del esquema
        message["schema_version"] = "1.0"
        # Serializar el mensaje usando Avro
        buffer = io.BytesIO()
        writer(buffer, self.avro_schema, [message])
        data = buffer.getvalue()
        producer = self.get_producer(topic)
        producer.send(data)
