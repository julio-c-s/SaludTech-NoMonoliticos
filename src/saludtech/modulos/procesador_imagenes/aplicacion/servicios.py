from saludtech.config.db import get_db
from saludtech.modulos.procesador_imagenes.infraestructura.repositorios import RepositorioImagenesSQL
from saludtech.modulos.procesador_imagenes.aplicacion.mapeadores import MapeadorImagenMedicaDTOJson
from saludtech.modulos.procesador_imagenes.dominio.fabricas import FabricaImagenes

class ServicioImagenMedica:
    def __init__(self):
        # Se obtiene la sesión de base de datos
        self.session = get_db()
        # Se crea el repositorio usando la sesión
        self.repositorio = RepositorioImagenesSQL(self.session)
        # Se instancia el mapeador
        self.mapeador = MapeadorImagenMedicaDTOJson()
        # Se instancia la fábrica para crear la entidad de dominio
        self.fabrica = FabricaImagenes()

    def registrar_imagen(self, imagen_dto):
        # La fábrica se encarga de convertir el objeto (ya sea dict o entidad) en una instancia de ImagenMedica.
        imagen = self.fabrica.crear_objeto(imagen_dto, self.mapeador)
        # Ahora se garantiza que 'imagen' es una instancia de ImagenMedica
        self.repositorio.guardar(imagen)
        # Se retorna la imagen convertida a dict para la respuesta (usando el mapeador)
        return self.mapeador.entidad_a_dto(imagen)
