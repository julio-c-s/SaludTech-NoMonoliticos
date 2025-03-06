from notificador.modulos.notificador.dominio.entidades import Notificacion

def mapear_a_entidad(registro) -> Notificacion:
    """
    Convierte un registro ORM a una instancia de Notificacion.
    Se asume que 'registro' posee atributos: id, mensaje, destinatario y estado_envio.
    """

    return Notificacion(registro.id, registro.mensaje, registro.destinatario, registro.estado_envio)

def mapear_a_registro(notificacion: Notificacion) -> dict:
    """
    Convierte una instancia de Notificacion a un diccionario para persistencia.
    """
    return {
        "id": notificacion.id,
        "mensaje": notificacion.mensaje,
        "destinatario": notificacion.destinatario,
        "estado_envio": notificacion.estado_envio
   }