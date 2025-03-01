from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ImagenAnonimizadaModel(db.Model):
    __tablename__ = 'imagenes_medicas'
    
    id = db.Column(db.String, primary_key=True)  # Usamos string para coincidir con el dominio
    url = db.Column(db.String(256), unique=True, nullable=False)
    modalidad = db.Column(db.String(64), nullable=False)
    region_anatomica = db.Column(db.String(64), nullable=False)
    patologia = db.Column(db.String(64), nullable=False)
    estado_procesamiento = db.Column(db.String(32), nullable=False, default="pendiente")
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ImagenAnonimizadaModel {self.id}>"
    
def importar_modelos_alchemy():
    import saludtech.modulos.anonimizador.infraestructura.modelos
