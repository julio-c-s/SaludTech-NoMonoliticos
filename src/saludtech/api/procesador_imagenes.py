import json
import saludtech.seedwork.presentacion.api as api
from flask import redirect, render_template, request, session, url_for, Response
from saludtech.modulos.procesador_imagenes.aplicacion.servicios import ServicioImagenMedica
# from saludtech.modulos.procesador_imagenes.aplicacion.dto import ImagenMedicaDTO
from saludtech.seedwork.dominio.excepciones import ExcepcionDominio
from saludtech.modulos.procesador_imagenes.aplicacion.mapeadores import MapeadorImagenMedicaDTOJson
from saludtech.modulos.procesador_imagenes.infraestructura.repositorios import RepositorioImagenesSQL

bp = api.crear_blueprint('procesador_imagenes', '/procesador_imagenes')

@bp.route('/imagen', methods=('POST',))
def registrar_imagen():
    try:
        # Read JSON data from the request
        imagen_dict = request.json
        servicio = ServicioImagenMedica()
        
        # Use the mapper to convert external JSON to a DTO
        map_imagen = MapeadorImagenMedicaDTOJson()
        imagen_dto = map_imagen.externo_a_dto(imagen_dict)
        
        # Initialize the service (adjust constructor if dependencies are needed)
        dto_final = servicio.registrar_imagen(imagen_dto)
        
        # Convert the resulting DTO back to external JSON format and return it
        return map_imagen.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        error_response = json.dumps({"error": str(e)})
        return Response(error_response, status=400, mimetype='application/json')

@bp.route('/imagen', methods=('GET',))
@bp.route('/imagen/<id>', methods=('GET',))
def obtener_imagen(id=None):
    if id:
        # Assuming your service has a method to get an image by its id.
        servicio = RegistrarImagenMedicaServicio()
        return servicio.obtener_imagen_por_id(id)
    else:
        # For now, return a simple message or list; adjust as needed.
        return [{"message": "Endpoint GET for imagen sin id not implemented yet"}]
