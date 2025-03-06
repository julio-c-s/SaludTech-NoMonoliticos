from dataclasses import dataclass
from anonimizador.seedwork.dominio.fabricas import Fabrica
from anonimizador.modulos.anonimizador.dominio.entidades import ImagenAnonimizada

@dataclass
class _FabricaImagenAnonimizada(Fabrica):
    def crear_objeto(self, obj: any, mapeador) -> any:
        # Si el objeto ya es una instancia de ImagenAnonimizada, se retorna directamente.
        if isinstance(obj, ImagenAnonimizada):
            return obj
        # De lo contrario, se asume que es un DTO (dict) y se convierte a entidad.
        return mapeador.dto_a_entidad(obj)

@dataclass
class FabricaImagenes(Fabrica):
    def crear_objeto(self, obj: any, mapeador) -> any:
        return _FabricaImagenAnonimizada().crear_objeto(obj, mapeador)
