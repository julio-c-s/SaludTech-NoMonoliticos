from saludtech.domain.events import ImageProcessedEvent

class ImageProcessingService:
    """
    Orquestador que aplica la lógica de negocio para procesar una imagen.
    Separa la capa de dominio (entidad y eventos) de la infraestructura.
    """
    def __init__(self, repository, event_bus):
        self.repository = repository
        self.event_bus = event_bus

    def process_image(self, image_id: str):
        # 1. Recuperar la imagen desde el repositorio
        image = self.repository.get_by_id(image_id)
        if not image:
            raise ValueError(f"No se encontró la imagen con ID {image_id}")

        # 2. Marcar la imagen como 'processing'
        image.mark_processing()
        self.repository.update(image)

        # 3. Simular procesamiento (p. ej., aplicar filtros, diagnósticos, etc.)
        #    En un caso real, aquí llamarías a librerías de procesamiento.
        diagnosis_result = {
            "resultado": "Procesado correctamente",
            "detalles": "Diagnóstico simulado"
        }

        # 4. Marcar la imagen como 'processed'
        image.mark_processed(diagnosis_result)
        self.repository.update(image)

        # 5. Publicar el evento de dominio
        event = ImageProcessedEvent(image_id=image.id, diagnosis=diagnosis_result)
        self.event_bus.publish(event)
        return image
