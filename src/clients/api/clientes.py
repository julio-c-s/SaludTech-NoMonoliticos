import clients.seedwork.presentacion.api as api
import json
from clients.modulos.vuelos.aplicacion.servicios import ServicioReserva
from clients.modulos.vuelos.aplicacion.dto import ReservaDTO
from clients.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from clients.modulos.vuelos.aplicacion.mapeadores import MapeadorReservaDTOJson
from clients.modulos.vuelos.aplicacion.comandos.crear_reserva import CrearReserva
from clients.seedwork.aplicacion.comandos import ejecutar_commando
from clients.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('clientes', '/clientes')

@bp.route('/reserva', methods=('POST',))
def reservar():
    try:
        reserva_dict = request.json

        map_reserva = MapeadorReservaDTOJson()
        reserva_dto = map_reserva.externo_a_dto(reserva_dict)

        sr = ServicioReserva()
        dto_final = sr.crear_reserva(reserva_dto)

        return map_reserva.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/reserva-comando', methods=('POST',))
def reservar_asincrona():
    try:
        reserva_dict = request.json

        map_reserva = MapeadorReservaDTOJson()
        reserva_dto = map_reserva.externo_a_dto(reserva_dict)

        comando = CrearReserva(reserva_dto.fecha_creacion, reserva_dto.fecha_actualizacion, reserva_dto.id, reserva_dto.itinerarios)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/reserva', methods=('GET',))
@bp.route('/reserva/<id>', methods=('GET',))
def dar_reserva(id=None):
    if id:
        sr = ServicioReserva()
        map_reserva = MapeadorReservaDTOJson()
        
        return map_reserva.dto_a_externo(sr.obtener_reserva_por_id(id))
    else:
        return [{'message': 'GET!'}]

@bp.route('/clientes-query', methods=('GET',))
def dar_reserva_usando_query(id=None):
    estado_procesamiento = request.args.get('estado_procesamiento')
    query_resultado = ejecutar_query(estado_procesamiento)
    map_reserva = MapeadorReservaDTOJson()
    return map_reserva.dto_externo(query_resultado)
    # return query_resultado