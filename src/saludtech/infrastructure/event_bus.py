class SimpleEventBus:
    """
    Implementación mínima de un bus de eventos que permite suscribir
    handlers y publicar eventos. Para un sistema productivo se usaría
    un broker como Kafka, RabbitMQ, etc.
    """
    def __init__(self):
        self.subscribers = []

    def subscribe(self, handler):
        self.subscribers.append(handler)

    def publish(self, event):
        print(f"Publicando evento: {event}")
        for handler in self.subscribers:
            handler(event)
