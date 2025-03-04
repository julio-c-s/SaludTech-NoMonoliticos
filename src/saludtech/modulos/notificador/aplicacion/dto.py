class MensajeNotificadorDTO:
    def __init__(self, mensaje: str, destinatario: str, estado_envio: str = "pendiente"):
        self.estado_envio = estado_envio
        self.mensaje = mensaje
        self.destinatario = destinatario