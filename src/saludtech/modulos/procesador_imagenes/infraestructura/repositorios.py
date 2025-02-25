from saludtech.modulos.procesador_imagenes.dominio.repositorio import RepositorioImagenes
from saludtech.modulos.procesador_imagenes.infraestructura.excepciones import RepositorioException
from saludtech.modulos.procesador_imagenes.infraestructura.mapeadores import mapear_a_entidad, mapear_a_registro

# Import the ORM model. Ensure that this model is defined to match your ImagenMedica entity.
from saludtech.modulos.procesador_imagenes.infraestructura.modelos import ImagenMedicaModel


class RepositorioImagenesSQL(RepositorioImagenes):
    def __init__(self, session):
        self.session = session
        self._tabla = ImagenMedicaModel

    def obtener_por_id(self, id_imagen):
        print("LLEgue a obetenrpor id repo")
        try:
            registro = self.session.query(self._tabla).filter_by(id=id_imagen).first()
            if registro:
                print("Registro")
                return mapear_a_entidad(registro)
            
            return None
        except Exception as e:
            print("Registro", e)
            raise RepositorioException(f"Error al obtener imagen por id: {str(e)}")

    def obtener_por_url(self, url):
        try:
            registro = self.session.query(self._tabla).filter_by(url=url).first()
            if registro:
                return mapear_a_entidad(registro)
            return None
        except Exception as e:
            raise RepositorioException(f"Error al obtener imagen por url: {str(e)}")

    def guardar(self, imagen):
        try:
            data = mapear_a_registro(imagen)
            # Create an ORM model instance using the mapped data.
            registro = self._tabla(**data)
            self.session.add(registro)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise RepositorioException(f"Error al guardar la imagen: {str(e)}")

    def eliminar(self, id_imagen):
        try:
            registro = self.session.query(self._tabla).filter_by(id=id_imagen).first()
            if registro:
                self.session.delete(registro)
                self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise RepositorioException(f"Error al eliminar la imagen: {str(e)}")
