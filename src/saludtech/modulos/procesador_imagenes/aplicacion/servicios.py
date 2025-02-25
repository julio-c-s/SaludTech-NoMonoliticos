from saludtech.seedwork.aplicacion.servicios import Servicio
from saludtech.modulos.procesador_imagenes.dominio.entidades import ImagenMedica
from saludtech.modulos.procesador_imagenes.dominio.fabricas import FabricaImagenes
from saludtech.modulos.procesador_imagenes.infraestructura.fabricas import FabricaRepositorio
from saludtech.modulos.procesador_imagenes.infraestructura.repositorios import RepositorioImagenesSQL
from .mapeadores import MapeadorImagenMedicaDTOJson
from .dto import ImagenMedicaDTO

class ServicioImagenMedica(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_imagenes: FabricaImagenes = FabricaImagenes()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_imagenes(self):
        return self._fabrica_imagenes

    def registrar_imagen(self, imagen_dto: ImagenMedicaDTO) -> ImagenMedicaDTO:
        # Create a domain entity (ImagenMedica) from the DTO using the mapper
        imagen: ImagenMedica = self.fabrica_imagenes.crear_objeto(imagen_dto, MapeadorImagenMedicaDTOJson())

        # Instantiate the repository using the repository factory
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenesSQL.__class__)
        repositorio.agregar(imagen)

        # Return a DTO representation of the created image
        return self.fabrica_imagenes.crear_objeto(imagen, MapeadorImagenMedicaDTOJson())

    def obtener_imagen_por_id(self, id) -> ImagenMedicaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenesSQL.__class__)
        imagen = repositorio.obtener_por_id(id)
        return self.fabrica_imagenes.crear_objeto(imagen, MapeadorImagenMedicaDTOJson())
