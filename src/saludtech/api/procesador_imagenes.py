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
    # Se obtiene el JSON enviado por el cliente.
    data = request.get_json()
    # Se instancia el mapeador para convertir el JSON a una entidad de dominio.
    map_imagen = MapeadorImagenMedicaDTOJson()
    # El método externo_a_dto utiliza dto_a_entidad para obtener una instancia de ImagenMedica.
    imagen_dto = map_imagen.externo_a_dto(data)
    # Se instancia el servicio
    servicio = ServicioImagenMedica()
    # Se registra la imagen y se obtiene la respuesta en formato dict.
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
        # Aquí podrías implementar la lógica para obtener todas las imágenes,
        # pero por ahora se retorna un mensaje indicándolo.
        return jsonify({"message": "Endpoint GET para imagen sin ID no implementado aún"}), 200