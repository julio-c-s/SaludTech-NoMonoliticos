from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class NotificacionModel(db.Model):
    __tablename__ = 'notificaciones'
    
    id = db.Column(db.String, primary_key=True)
    mensaje = db.Column(db.String, nullable=False)
    destinatario = db.Column(db.String, nullable=False)
    estado_envio = db.Column(db.String(32), nullable=False, default="pendiente")
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<NotificacionModel {self.id}>"
    
def importar_modelos_alchemy():
    import saludtech.modulos.notificador.infraestructura.modelos