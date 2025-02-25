import json
import saludtech.seedwork.presentacion.api as api
from flask import redirect, render_template, request, session, url_for, Response,jsonify
from saludtech.modulos.procesador_imagenes.aplicacion.servicios import ServicioImagenMedica
# from saludtech.modulos.procesador_imagenes.aplicacion.dto import ImagenMedicaDTO
from saludtech.seedwork.dominio.excepciones import ExcepcionDominio
from saludtech.modulos.procesador_imagenes.aplicacion.mapeadores import MapeadorImagenMedicaDTOJson
from saludtech.modulos.procesador_imagenes.infraestructura.repositorios import RepositorioImagenesSQL

bp = api.crear_blueprint('procesador_imagenes', '/procesador_imagenes')

@bp.route('/imagen', methods=['POST'])
def registrar_imagen():

    data = request.get_json()
   
    map_imagen = MapeadorImagenMedicaDTOJson()

    imagen_dto = map_imagen.externo_a_dto(data)

    servicio = ServicioImagenMedica()

    dto_final = servicio.registrar_imagen(imagen_dto)
    return jsonify(dto_final), 201



@bp.route('/imagen', methods=['GET'])
@bp.route('/imagen/<string:id>', methods=['GET'])
def obtener_imagen(id=None):
    servicio = ServicioImagenMedica()
    if id:
        try:
            imagen = servicio.obtener_imagen_por_id(id)
            if imagen is None:
                return jsonify({"message": "Imagen no encontrada"}), 404
            return jsonify(imagen), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:

        return jsonify({"message": "Endpoint GET para imagen sin ID no implementado aún"}), 200