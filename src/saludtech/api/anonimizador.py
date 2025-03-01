import json
import saludtech.seedwork.presentacion.api as api
from flask import redirect, render_template, request, session, url_for, Response,jsonify
from saludtech.modulos.anonimizador.aplicacion.servicios import ServicioImagenAnonimizada
# from saludtech.modulos.anonimizador.aplicacion.dto import ImagenAnonimizadaDTO
from saludtech.seedwork.dominio.excepciones import ExcepcionDominio
from saludtech.modulos.anonimizador.aplicacion.mapeadores import MapeadorImagenAnonimizadaDTOJson
from saludtech.modulos.anonimizador.infraestructura.repositorios import RepositorioImagenesSQL

bp = api.crear_blueprint('anonimizador', '/anonimizador')

@bp.route('/imagen', methods=['POST'])
def registrar_imagen():

    data = request.get_json()
   
    map_imagen = MapeadorImagenAnonimizadaDTOJson()

    imagen_dto = map_imagen.externo_a_dto(data)

    servicio = ServicioImagenAnonimizada()

    dto_final = servicio.registrar_imagen(imagen_dto)
    return jsonify(dto_final), 201

@bp.route('/imagen/<string:id>', methods=['GET'])
def obtener_imagen(id=None):
    servicio = ServicioImagenAnonimizada()
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
    servicio = ServicioImagenAnonimizada()
    imagenes = servicio.obtener_todas_las_imagenes()
    return jsonify(imagenes), 200

@bp.route('/imagen/<string:id>', methods=['PUT'])
def actualizar_imagen(id=None):
    data = request.get_json()
    map_imagen = MapeadorImagenAnonimizadaDTOJson()
    imagen_dto = map_imagen.externo_a_dto(data)
    servicio = ServicioImagenAnonimizada()
    dto_final = servicio.actualizar_imagen(imagen_dto)
    return jsonify(dto_final), 200

@bp.route('/imagen/<string:id>', methods=['DELETE'])
def eliminar_imagen(id=None):
    servicio = ServicioImagenAnonimizada()
    servicio.eliminar_imagen(id)
    return jsonify({"message": "Imagen eliminada"}), 200
