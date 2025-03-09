# src/saludtech/aplicacion/saga_coordinator.py
from datetime import datetime
from dataclasses import asdict
from saludtech.modulos.procesador.dominio.eventos import ImagenRegistradaSaga, ImagenRegistroCompensado
from saludtech.modulos.procesador.infraestructura.pulsar_client import PulsarClient
from saludtech.config.db import get_db
from saludtech.modulos.procesador.infraestructura.repositorios import RepositorioImagenesSQL

class SagaCoordinator:
    def __init__(self):
        # Inicializa el cliente de Pulsar
        self.pulsar_client = PulsarClient()
        # Opcionalmente, inicializa el Saga Log (puede ser un repositorio, base de datos o archivo)
        self.saga_log = []  # Simple lista como ejemplo

    def iniciar_saga_registro_imagen(self, imagen):
        """
        Inicia la saga para el registro de una imagen. Este método:
          - Registra la imagen en la base de datos.
          - Publica un evento de inicio de saga.
          - Registra el evento en el Saga Log.
        """
        # Aquí se podría realizar la lógica de negocio inicial (ej. guardar la imagen)
        repositorio = RepositorioImagenesSQL(get_db())
        repositorio.guardar(imagen)
        
        # Crea el evento de inicio de la saga (debes definir ImagenRegistradaSaga en tu dominio)
        evento = ImagenRegistradaSaga(
            timestamp=datetime.now(),
            imagen_id=imagen.id,
            ruta_archivo=imagen.url
        )
        # Publica el evento en un tópico específico para sagas (por ejemplo, "sagas.imagen")
        self.pulsar_client.publish_event("sagas.imagen", asdict(evento))
        
        # Registra el evento en el Saga Log (aquí lo simulamos con una lista)
        self.saga_log.append(asdict(evento))
        return evento

    def compensar_registro_imagen(self, imagen_id, motivo):
        """
        Ejecuta una acción compensatoria en caso de fallo en la saga.
        """
        evento = ImagenRegistroCompensado(
            timestamp=datetime.now(),
            imagen_id=imagen_id,
            motivo=motivo
        )
        self.pulsar_client.publish_event("sagas.imagen", asdict(evento))
        self.saga_log.append(asdict(evento))
        return evento
