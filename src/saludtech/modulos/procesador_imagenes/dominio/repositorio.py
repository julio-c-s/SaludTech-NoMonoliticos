from abc import ABC, abstractmethod

class RepositorioImagenes(ABC):

    @abstractmethod
    def obtener_por_id(self, id_imagen):
        pass

    @abstractmethod
    def obtener_por_url(self, url):
        pass

    @abstractmethod
    def guardar(self, imagen):
        pass

    @abstractmethod
    def eliminar(self, id_imagen):
        pass