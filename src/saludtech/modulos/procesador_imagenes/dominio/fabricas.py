from dataclasses import dataclass
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.modulos.procesador_imagenes.dominio.entidades import ImagenMedica

@dataclass
class _FabricaImagenMedica(Fabrica):
    def crear_objeto(self, obj: any, mapeador) -> any:
        # Si el objeto ya es una instancia de ImagenMedica, se retorna directamente.
        if isinstance(obj, ImagenMedica):
            return obj
        # De lo contrario, se asume que es un DTO (dict) y se convierte a entidad.
        return mapeador.dto_a_entidad(obj)

@dataclass
class FabricaImagenes(Fabrica):
    def crear_objeto(self, obj: any, mapeador) -> any:
        return _FabricaImagenMedica().crear_objeto(obj, mapeador)
