import pulsar
from pulsar.schema import *

class Despachador:
    async def publicar_mensaje(self, mensaje, topico):
        cliente = pulsar.Client("pulsar://localhost:6650")
        publicador = cliente.create_producer(topico)
        publicador.send(mensaje)
        cliente.close()
