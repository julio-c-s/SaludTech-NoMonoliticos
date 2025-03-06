from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ImagenAnonimizadaModel(db.Model):
    __tablename__ = 'imagenes_anonimizadas'
    
    id = db.Column(db.String, primary_key=True)
    id_imagen_original = db.Column(db.String, nullable=False)
    url_imagen_original = db.Column(db.String, nullable=False)
    url_imagen_anonimizada = db.Column(db.String, nullable=True)
    estado_procesamiento = db.Column(db.String(32), nullable=False, default="pendiente")
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ImagenAnonimizadaModel {self.id}>"
    
def importar_modelos_alchemy():
    import saludtech.modulos.anonimizador.infraestructura.modelos
