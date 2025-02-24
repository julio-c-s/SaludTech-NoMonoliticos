from saludtech.config.db import db
from uuid import uuid4

class ImageModel(db.Model):
    """
    Modelo ORM que mapea la entidad de dominio 'Image' a la tabla 'images'.
    """
    __tablename__ = 'images'

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    status = db.Column(db.String, nullable=False, default="pending")
    image_metadata = db.Column(db.JSON, nullable=True)
    diagnosis = db.Column(db.JSON, nullable=True)

class ImageRepository:
    """
    Repositorio que abstrae las operaciones de persistencia.
    """
    def create(self, image_domain):
        model = ImageModel(
            id=image_domain.id,
            status=image_domain.status,
            image_metadata=image_domain.image_metadata,
            diagnosis=image_domain.diagnosis
        )
        db.session.add(model)
        db.session.commit()
        return model

    def get_by_id(self, image_id):
        model = ImageModel.query.get(image_id)
        return model

    def update(self, image_domain):
        model = ImageModel.query.get(image_domain.id)
        if not model:
            return None
        model.status = image_domain.status
        model.image_metadata = image_domain.image_metadata
        model.diagnosis = image_domain.diagnosis
        db.session.commit()
        return model
