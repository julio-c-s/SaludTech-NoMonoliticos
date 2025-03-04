from functools import singledispatch
from abc import ABC, abstractmethod
from dataclasses import dataclass
from clients.seedwork.aplicacion.servicios import Servicio
from clients.modulos.vuelos.dominio.entidades import Reserva
from clients.modulos.vuelos.dominio.fabricas import FabricaVuelos
from clients.modulos.cliente.infraestructura.fabricas import FabricaRepositorio
from clients.modulos.vuelos.infraestructura.repositorios import RepositorioReservas
from clients.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from clients.modulos.vuelos.aplicacion.mapeadores import MapeadorReserva

from clients.modulos.vuelos.aplicacion.dto import ReservaDTO


class ServicioCliente(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_vuelos: FabricaVuelos = FabricaVuelos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos

    def obtener_reserva_por_id(self, id) -> ReservaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)
        return self.fabrica_vuelos.crear_objeto(repositorio.obtener_por_id(id), MapeadorReserva())
    
    def obtener_reserva_por_estado_procesamiento(self, id) -> ReservaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas.__class__)
        # return self.fabrica_vuelos.crear_objeto(repositorio.obtener_por_estado_procesamiento(id), MapeadorReserva())
        print("repositorio.obtener_por_estado_procesamiento(id)")
        print(repositorio.obtener_por_estado_procesamiento(id))
        return repositorio.obtener_por_estado_procesamiento(id)


class Query(ABC):
    ...

@dataclass
class QueryResultado:
    resultado: None

class QueryHandler(ABC):
    @abstractmethod
    def handle(self, query: Query) -> QueryResultado:
        raise NotImplementedError()

@singledispatch
def ejecutar_query(query):
    sr = ServicioCliente()
    print("ejecutar_query(query)" + query)
    return sr.obtener_reserva_por_estado_procesamiento(query)
