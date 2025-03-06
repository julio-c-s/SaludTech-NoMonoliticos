import json
from uuid import UUID
import anonimizador.seedwork.presentacion.api as api
from flask import redirect, render_template, request, session, url_for, Response,jsonify
from anonimizador.modulos.anonimizador.aplicacion.servicios import ServicioImagenAnonimizada
# from saludtech.modulos.anonimizador.aplicacion.dto import ImagenAnonimizadaDTO
from anonimizador.seedwork.dominio.excepciones import ExcepcionDominio
from anonimizador.modulos.anonimizador.aplicacion.mapeadores import MapeadorImagenAnonimizadaDTOJson
from anonimizador.modulos.anonimizador.infraestructura.repositorios import RepositorioImagenesSQL

bp = api.crear_blueprint('anonimizador', '/anonimizador')

@bp.route('/imagen', methods=['POST'])
def registrar_imagen():
    data = request.get_json()
    map_imagen = MapeadorImagenAnonimizadaDTOJson()
    try:
        imagen_dto = map_imagen.externo_a_dto(data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    servicio = ServicioImagenAnonimizada()
    dto_final = servicio.registrar_imagen(imagen_dto)
    return jsonify(dto_final), 201


@bp.route('/imagen/<string:id>', methods=['GET'])
def obtener_imagen(id=None):
    servicio = ServicioImagenAnonimizada()
    if id:
        try:
            id_uuid = UUID(id)
        except ValueError:
            return jsonify({"error": "ID inválido, debe ser un UUID"}), 400
        
        try:
            imagen = servicio.obtener_imagen(str(id_uuid))
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

@bp.route('/imagen/<string:id>', methods=['PUT'])  # Cambiar de <uuid:id> a <string:id> para evitar problemas de conversión
def actualizar_imagen(id):
    data = request.get_json()
    map_imagen = MapeadorImagenAnonimizadaDTOJson()
    servicio = ServicioImagenAnonimizada()

    try:
        imagen_existente = servicio.obtener_imagen(id)
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

    try:
        imagen_dto = map_imagen.dto_a_entidad(data, imagen_existente)
    except Exception as e:
        return jsonify({"error": f"Error en mapeo DTO: {str(e)}"}), 400

    # Verificación de ID antes de actualizar
    if str(imagen_dto.id) != str(imagen_existente.id):
        return jsonify({"error": "El ID en el cuerpo de la solicitud no coincide con el ID en la base de datos"}), 400

    try:
        dto_final = servicio.actualizar_imagen(imagen_dto)
        return jsonify(dto_final), 200
    except Exception as e:
        return jsonify({"error": f"Error en la actualización: {str(e)}"}), 500


@bp.route('/imagen/<string:id>', methods=['DELETE'])
def eliminar_imagen(id=None):
    servicio = ServicioImagenAnonimizada()
    servicio.eliminar_imagen(id)
    return jsonify({"message": "Imagen eliminada"}), 200
