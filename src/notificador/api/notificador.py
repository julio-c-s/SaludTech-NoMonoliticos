import saludtech.seedwork.presentacion.api as api
from flask import request, jsonify
from saludtech.modulos.notificador.aplicacion.servicios import ServicioNotificaciones

bp = api.crear_blueprint('notificador', '/notificador')

@bp.route('/notificacion', methods=['POST'])
def enviar_notificacion():
    data = request.get_json()
    servicio = ServicioNotificaciones()
    notificacion = servicio.enviar_notificacion(data)
    return jsonify(notificacion), 201

@bp.route('/notificacion/<string:id>', methods=['GET'])
def obtener_notificacion(id):
    servicio = ServicioNotificaciones()
    notificacion = servicio.obtener_notificacion(id)
    return jsonify(notificacion), 200

@bp.route('/notificacion', methods=['GET'])
def obtener_notificaciones():
    servicio = ServicioNotificaciones()
    notificaciones = servicio.obtener_todas_las_notificaciones()
    return jsonify(notificaciones), 200

@bp.route('/notificacion/<string:id>', methods=['PUT'])
def actualizar_notificacion(id):
    data = request.get_json()
    servicio = ServicioNotificaciones()
    notificacion = servicio.actualizar_notificacion(data)
    return jsonify(notificacion), 200

@bp.route('/notificacion/<string:id>', methods=['DELETE'])
def eliminar_notificacion(id):
    servicio = ServicioNotificaciones()
    servicio.eliminar_notificacion(id)
    return jsonify({"message": "Notificación eliminada correctamente"}), 200