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


@bp.route('/imagen', methods=('GET',))
@bp.route('/imagen/<id>', methods=('GET',))
def obtener_imagen(id):
    servicio = ServicioImagenMedica()
    imagen_dto = servicio.obtener_imagen_por_id(id)
    if imagen_dto is None:
        return jsonify({"error": "Imagen no encontrada"}), 404

    map_imagen = MapeadorImagenMedicaDTOJson()
    return jsonify(map_imagen.entidad_a_dto(imagen_dto))
