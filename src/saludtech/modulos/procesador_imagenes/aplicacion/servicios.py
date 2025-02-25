from saludtech.config.db import get_db
from saludtech.modulos.procesador_imagenes.infraestructura.repositorios import RepositorioImagenesSQL
from saludtech.modulos.procesador_imagenes.aplicacion.mapeadores import MapeadorImagenMedicaDTOJson
from saludtech.modulos.procesador_imagenes.dominio.fabricas import FabricaImagenes

class ServicioImagenMedica:
    def __init__(self):
        self.session = get_db()
        self.repositorio = RepositorioImagenesSQL(self.session)
        self.mapeador = MapeadorImagenMedicaDTOJson()
        self.fabrica = FabricaImagenes()

    def registrar_imagen(self, imagen_dto):
        # Convierto el DTO (dict) a una entidad de dominio usando la fábrica.
        imagen = self.fabrica.crear_objeto(imagen_dto, self.mapeador)
        # Ahora imagen es una instancia de ImagenMedica, por lo que mapear_a_registro funcionará correctamente.
        self.repositorio.guardar(imagen)
        return self.mapeador.entidad_a_dto(imagen)

    def obtener_imagen_por_id(self, id):
        # Recuperar la imagen desde el repositorio usando el atributo ya creado en __init__
        imagen = self.repositorio.obtener_por_id(id)
        if imagen is None:
            return None  # o bien lanzar una excepción, según tu lógica de negocio
        # Convertir la entidad de dominio a DTO usando el mapper ya definido
        return self.mapeador.entidad_a_dto(imagen)