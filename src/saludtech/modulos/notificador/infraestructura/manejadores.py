from saludtech.modulos.notificador.dominio.eventos import NotificacionEliminada, NotificacionEnviada, NotificacionFallida
from saludtech.modulos.notificador.infraestructura.event_dispatcher import dispatcher

def manejar_notificacion_enviada(evento: NotificacionEnviada):
    print(f"📢 Notificación enviada: ID {evento.id} | Usuario {evento.usuario_id} | Mensaje {evento.mensaje}"
            f" | Destinatario {evento.destinatario}")
    
def manejar_notificacion_fallida(evento: NotificacionFallida):
    print(f"⚠️ Error enviando notificación: ID {evento.id} | Error: {evento.mensaje_error}")

def manejar_notificacion_eliminada(evento: NotificacionEliminada):
    print(f"🗑️ Notificación eliminada: ID {evento.id} | Usuario {evento.usuario_id} | Motivo: {evento.motivo}"
            f" | Destinatario {evento.destinatario}")
    
# Suscribir los manejadores a los eventos
dispatcher.suscribir(NotificacionEnviada, manejar_notificacion_enviada)
dispatcher.suscribir(NotificacionFallida, manejar_notificacion_fallida)
dispatcher.suscribir(NotificacionEliminada, manejar_notificacion_eliminada)

