from notificador.modulos.notificador.dominio.repositorio import RepositorioNotificaciones
from notificador.modulos.notificador.infraestructura.excepciones import RepositorioException
from notificador.modulos.notificador.infraestructura.mapeadores import mapear_a_entidad, mapear_a_registro
from notificador.modulos.notificador.infraestructura.modelos import NotificacionModel


class RepositorioNotificacionesSQL(RepositorioNotificaciones):
    def __init__(self, session):
        self.session = session
        self._tabla = NotificacionModel
    
    def obtener_por_id(self, id_notificacion):
        try:
            registro = self.session.query(self._tabla).filter_by(id=id_notificacion).first()
            if registro:
                return mapear_a_entidad(registro)
            
            return None
        except Exception as e:
            raise RepositorioException(f"Error al obtener notificacion por id: {str(e)}")
        
    def obtener_todos(self):
        try:
            registros = self.session.query(self._tabla).all()
            return [mapear_a_entidad(registro) for registro in registros]
        except Exception as e:
            raise RepositorioException(f"Error al obtener todas las notificaciones: {str(e)}")
        
    def guardar(self, notificacion):
        try:
            data = mapear_a_registro(notificacion)
            registro = self._tabla(**data)
            self.session.add(registro)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise RepositorioException(f"Error al guardar la notificacion: {str(e)}")
    
    def actualizar(self, notificacion):
        try:
            data = mapear_a_registro(notificacion)
            registro = self.session.query(self._tabla).filter_by(id=notificacion.id).first()
            
            if registro:
                for key, value in data.items():
                    setattr(registro, key, value)
            else:
                print(f"[ERROR] No se encontró la notificacion con ID: {notificacion.id}, podría estar intentando insertar una nueva.")
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise RepositorioException(f"Error al actualizar la notificacion: {str(e)}")
        
    def eliminar(self, id_notificacion):
        try:
            registro = self.session.query(self._tabla).filter_by(id=id_notificacion).first()
            if registro:
                self.session.delete(registro)
                self.session.commit()
            else:
                print(f"[ERROR] No se encontró la notificacion con ID: {id_notificacion}, no se puede eliminar.")
        except Exception as e:
            self.session.rollback()
            raise RepositorioException(f"Error al eliminar la notificacion: {str(e)}")
        