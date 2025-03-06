from saludtech.modulos.anonimizador.dominio.repositorio import RepositorioImagenes
from saludtech.modulos.anonimizador.infraestructura.excepciones import RepositorioException
from saludtech.modulos.anonimizador.infraestructura.mapeadores import mapear_a_entidad, mapear_a_registro

# Import the ORM model. Ensure that this model is defined to match your ImagenAnonimizada entity.
from saludtech.modulos.anonimizador.infraestructura.modelos import ImagenAnonimizadaModel


class RepositorioImagenesSQL(RepositorioImagenes):
    def __init__(self, session):
        self.session = session
        self._tabla = ImagenAnonimizadaModel

    def obtener_por_id(self, id_imagen):
        try:
            registro = self.session.query(self._tabla).filter_by(id=id_imagen).first()
            if registro:
                return mapear_a_entidad(registro)
            
            return None
        except Exception as e:
            raise RepositorioException(f"Error al obtener imagen por id: {str(e)}")

    def obtener_todos(self):
        try:
            registros = self.session.query(self._tabla).all()
            return [mapear_a_entidad(registro) for registro in registros]
        except Exception as e:
            raise RepositorioException(f"Error al obtener todas las imagenes: {str(e)}")

    # Misma funcion de Agregar
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
        
    def actualizar(self, imagen):
        try:
            data = mapear_a_registro(imagen)
            registro = self.session.query(self._tabla).filter_by(id=imagen.id).first()

            if registro:
                for key, value in data.items():
                    setattr(registro, key, value)
            else:
                print(f"[ERROR] No se encontró la imagen con ID: {imagen.id}, podría estar intentando insertar una nueva.")
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise RepositorioException(f"Error al actualizar la imagen: {str(e)}")


    def eliminar(self, id_imagen):
        try:
            registro = self.session.query(self._tabla).filter_by(id=id_imagen).first()
            if registro:
                self.session.delete(registro)
                self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise RepositorioException(f"Error al eliminar la imagen: {str(e)}")

    def obtener_por_url(self, url):
        try:
            registro = self.session.query(self._tabla).filter_by(url=url).first()
            if registro:
                return mapear_a_entidad(registro)
            return None
        except Exception as e:
            raise RepositorioException(f"Error al obtener imagen por url: {str(e)}")