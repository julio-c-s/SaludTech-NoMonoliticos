from flask import Blueprint, request, jsonify
from saludtech.infrastructure.repository import ImageRepository, ImageModel
from saludtech.infrastructure.event_bus import SimpleEventBus
from saludtech.application.image_service import ImageProcessingService
from saludtech.domain.image import Image

image_bp = Blueprint('image_bp', __name__)

# Instanciamos el repositorio y el bus de eventos
repo = ImageRepository()
bus = SimpleEventBus()

# Suscripción de un handler simple para eventos de dominio
def image_processed_handler(event):
    print(f"[Handler] Se recibió un evento de imagen procesada: {event}")

bus.subscribe(image_processed_handler)

# Creamos el servicio de aplicación
image_service = ImageProcessingService(repo, bus)

@image_bp.route('/images', methods=['POST'])
def create_image():
    """
    Crea una imagen en estado 'pending'.
    Body esperado (JSON):
    {
      "image_metadata": { ... }
    }
    """
    data = request.json or {}
    image_metadata = data.get("image_metadata", {})

    # Instanciamos la entidad de dominio
    new_image_domain = Image(image_metadata=image_metadata)
    # Persistimos usando el repositorio
    model = repo.create(new_image_domain)
    return jsonify({
        "id": model.id,
        "status": model.status,
        "image_metadata": model.image_metadata
    }), 201

@image_bp.route('/images/<image_id>/process', methods=['POST'])
def process_image(image_id):
    """
    Inicia el procesamiento de la imagen con el ID dado.
    """
    image_service.process_image(image_id)
    return jsonify({"message": f"Procesando imagen {image_id}"}), 200

@image_bp.route('/images/<image_id>', methods=['GET'])
def get_image(image_id):
    """
    Retorna los datos de la imagen con el ID especificado.
    """
    model = repo.get_by_id(image_id)
    if not model:
        return jsonify({"error": "Image not found"}), 404

    return jsonify({
        "id": model.id,
        "status": model.status,
        "image_metadata": model.image_image_metadata,
        "diagnosis": model.diagnosis
    }), 200
