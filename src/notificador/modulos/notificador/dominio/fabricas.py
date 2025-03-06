from dataclasses import dataclass
from notificador.seedwork.dominio.fabricas import Fabrica
from notificador.modulos.notificador.dominio.entidades import Notificacion

@dataclass
class _FabricaNotificaciones(Fabrica):
    def crear_objeto(self, obj: any, mapeador) -> any:
        # Si el objeto ya es una instancia de Notificacion, se retorna directamente.
        if isinstance(obj, Notificacion):
            return obj
        # De lo contrario, se asume que es un DTO (dict) y se convierte a entidad.
        return mapeador.dto_a_entidad(obj)
    
@dataclass
class FabricaNotificaciones(Fabrica):
    def crear_objeto(self, obj: any, mapeador) -> any:
        return _FabricaNotificaciones().crear_objeto(obj, mapeador)