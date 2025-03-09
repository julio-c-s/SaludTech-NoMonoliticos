import pulsar, aiopulsar, asyncio

async def suscribirse_a_topico(topico, suscripcion, eventos=[]):
    async with aiopulsar.connect("pulsar://localhost:6650") as cliente:
        async with cliente.subscribe(topico, subscription_name=suscripcion) as consumidor:
            while True:
                mensaje = await consumidor.receive()
                eventos.append(str(mensaje.value()))
                await consumidor.acknowledge(mensaje)
