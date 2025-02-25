from dataclasses import dataclass
from saludtech.seedwork.dominio.fabricas import Fabrica
from saludtech.seedwork.dominio.entidades import Entidad
from saludtech.modulos.procesador_imagenes.dominio.entidades import ImagenMedica

@dataclass
class _FabricaImagenMedica(Fabrica):
    def crear_objeto(self, obj: any, mapeador) -> any:
        # If obj is already a domain entity, convert it to a DTO using the mapper.
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            # Otherwise, assume obj is a DTO and convert it to a domain entity.
            return mapeador.dto_a_entidad(obj)

@dataclass
class FabricaImagenes(Fabrica):
    def crear_objeto(self, obj: any, mapeador) -> any:
        # We expect the mapper to work with ImagenMedica objects.
        if mapeador.obtener_tipo() == ImagenMedica.__class__:
            fabrica_imagen = _FabricaImagenMedica()
            return fabrica_imagen.crear_objeto(obj, mapeador)
        else:
            raise Exception("Tipo de objeto no existe en el dominio de imagenes")
