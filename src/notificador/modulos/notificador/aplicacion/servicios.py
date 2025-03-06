from datetime import datetime
from dataclasses import dataclass
from notificador.config.db import get_db
from notificador.modulos.notificador.infraestructura.repositorios import RepositorioNotificacionesSQL
from notificador.modulos.notificador.aplicacion.mapeadores import MapeadorNotificacionDTOJson
from notificador.modulos.notificador.dominio.fabricas import FabricaNotificaciones
from notificador.modulos.notificador.dominio.eventos import (
    NotificacionEnviada, NotificacionFallida
)
from notificador.modulos.notificador.infraestructura.event_dispatcher import dispatcher

class ServicioNotificaciones:
    def __init__(self):
        self.session = get_db()
        self.repositorio = RepositorioNotificacionesSQL(self.session)
        self.mapeador = MapeadorNotificacionDTOJson()
        self.fabrica = FabricaNotificaciones()

    def enviar_notificacion(self, notificacion_dto):
        notificacion = self.fabrica.crear_objeto(notificacion_dto, self.mapeador)
        if not hasattr(notificacion, 'id'):
            raise AttributeError("El objeto Notificacion debe contener un id")
        self.repositorio.guardar(notificacion)
        evento = NotificacionEnviada(
            timestamp=datetime.now(),
            id=notificacion.id,
            destinatario=notificacion.destinatario
        )
        dispatcher.publicar(evento)
        return self.mapeador.entidad_a_dto(notificacion)

    def obtener_notificacion(self, id_notificacion):
        notificacion = self.repositorio.obtener_por_id(id_notificacion)
        if not notificacion:
            raise ValueError(f"No se encontró la notificación con ID {id_notificacion}")
        return notificacion
    
    def obtener_todas_las_notificaciones(self):
        notificaciones = self.repositorio.obtener_todos()
        return [self.mapeador.entidad_a_dto(notificacion) for notificacion in notificaciones]
    
    def actualizar_notificacion(self, notificacion_dto):
        try:
            notificacion_existente = self.repositorio.obtener_por_id(notificacion_dto.id)

            if not notificacion_existente:
                raise ValueError(f"[ERROR] No se encontró la notificación con ID {notificacion_dto.id}.")

            # Actualizar los campos
            notificacion_existente.estado_envio = notificacion_dto.estado_envio

            print("Actualizando notificación en la base de datos...")  # Debugging
            self.repositorio.actualizar(notificacion_existente)
            print("Notificación actualizada correctamente.")  # Debugging

            # Disparar evento
            evento = NotificacionFallida(
                timestamp=datetime.now(),
                id=notificacion_existente.id,
                destinatario=notificacion_existente.destinatario
            )
            dispatcher.publicar(evento)
            return self.mapeador.entidad_a_dto(notificacion_existente)
        except Exception as e:
            print(f"[ERROR] Error al actualizar la notificación: {str(e)}")
            return None
        
    def eliminar_notificacion(self, id_notificacion):
        notificacion = self.repositorio.obtener_por_id(id_notificacion)
        if notificacion:
            evento = NotificacionFallida(
                timestamp=datetime.now(),
                id=id_notificacion,
                destinatario=notificacion.destinatario
            )
            dispatcher.publicar(evento)
        self.repositorio.eliminar(id_notificacion)
        return notificacion
    
    def obtener_por_id(self, id_notificacion):
        notificacion = self.repositorio.obtener_por_id(id_notificacion)
        if not notificacion:
            raise ValueError(f"No se encontró la notificación con ID {id_notificacion}")
        return notificacion