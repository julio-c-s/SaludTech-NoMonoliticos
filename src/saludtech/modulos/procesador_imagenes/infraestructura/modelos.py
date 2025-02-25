from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Se asume que la instancia de SQLAlchemy se inicializa en otro módulo
db = SQLAlchemy()

class ImagenMedicaModel(db.Model):
    __tablename__ = 'imagenes_medicas'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    url = db.Column(db.String(256), unique=True, nullable=False)
    ruta_archivo = db.Column(db.String(256), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<ImagenMedicaModel {self.nombre}>"
