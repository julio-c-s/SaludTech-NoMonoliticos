from abc import ABC, abstractmethod

class RepositorioNotificaciones(ABC):

    @abstractmethod
    def obtener_por_id(self, id_notificacion):
        pass

    @abstractmethod
    def guardar(self, notificacion):
        pass

    @abstractmethod
    def eliminar(self, id_notificacion):
        pass