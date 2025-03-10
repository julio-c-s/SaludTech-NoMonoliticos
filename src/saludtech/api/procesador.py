import json
import saludtech.seedwork.presentacion.api as api
from flask import redirect, render_template, request, session, url_for, Response,jsonify
from saludtech.modulos.procesador.aplicacion.servicios import ServicioImagenMedica
# from saludtech.modulos.procesador_imagenes.aplicacion.dto import ImagenMedicaDTO
from saludtech.seedwork.dominio.excepciones import ExcepcionDominio
from saludtech.modulos.procesador.aplicacion.mapeadores import MapeadorImagenMedicaDTOJson
from saludtech.modulos.procesador.infraestructura.repositorios import RepositorioImagenesSQL
from saludtech.modulos.sagas.aplicacion.global_vars import saga_coordinator_global  # La instancia global

bp = api.crear_blueprint('procesador_imagenes', '/procesador_imagenes')

@bp.route('/imagen', methods=['POST'])
def registrar_imagen():

    data = request.get_json()
   
    map_imagen = MapeadorImagenMedicaDTOJson()

    imagen_dto = map_imagen.externo_a_dto(data)

    servicio = ServicioImagenMedica()

    dto_final = servicio.registrar_imagen(imagen_dto)
    return jsonify(dto_final), 201

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
    
@bp.route('/imagen', methods=['GET'])
def obtener_imagenes():
    servicio = ServicioImagenMedica()
    imagenes = servicio.obtener_todas_las_imagenes()
    return jsonify(imagenes), 200

@bp.route('/imagen/<string:id>', methods=['PUT'])
def actualizar_imagen(id=None):
    data = request.get_json()
    map_imagen = MapeadorImagenMedicaDTOJson()
    imagen_dto = map_imagen.externo_a_dto(data)
    servicio = ServicioImagenMedica()
    dto_final = servicio.actualizar_imagen(imagen_dto)
    return jsonify(dto_final), 200

@bp.route('/imagen/<string:id>', methods=['DELETE'])
def eliminar_imagen(id=None):
    servicio = ServicioImagenMedica()
    servicio.eliminar_imagen(id)
    return jsonify({"message": "Imagen eliminada"}), 200


@bp.route('/saga_log', methods=['GET'])
def obtener_saga_log():
    log = saga_coordinator_global.obtener_saga_log()
    return jsonify(log), 200
