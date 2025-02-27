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
    
    def obtener_imagen_por_id(self, id_imagen):
            imagen = self.repositorio.obtener_por_id(id_imagen)
            if imagen is None:
                return None
            return self.mapeador.entidad_a_dto(imagen)
    
    def obtener_todas_las_imagenes(self):
        imagenes = self.repositorio.obtener_todos()
        return [self.mapeador.entidad_a_dto(imagen) for imagen in imagenes]
    
    def actualizar_imagen(self, imagen_dto):
        imagen = self.fabrica.crear_objeto(imagen_dto, self.mapeador)
        self.repositorio.actualizar(imagen)
        return self.mapeador.entidad_a_dto(imagen)
    
    def eliminar_imagen(self, id_imagen):
        self.repositorio.eliminar(id_imagen)
        
    def obtener_imagen_por_url(self, url):
        imagen = self.repositorio.obtener_por_url(url)
        if imagen is None:
            return None
        return self.mapeador.entidad_a_dto(imagen)