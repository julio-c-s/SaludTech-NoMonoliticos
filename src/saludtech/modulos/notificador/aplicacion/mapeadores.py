import uuid
from saludtech.modulos.notificador.dominio.entidades import Notificacion

class MapeadorNotificacionDTOJson:
    def obtener_tipo(self):
        return Notificacion
    
    def dto_a_entidad(self, dto, entidad_existente=None) -> Notificacion:
        """
        Convierte un DTO en una entidad Notificacion.
        """

        if entidad_existente:
            id_notificacion = entidad_existente.id
        else:
            id_notificacion = dto.get('id', str(uuid.uuid4()))

        mensaje = dto.get('mensaje', entidad_existente.mensaje if entidad_existente else '')
        destinatario = dto.get('destinatario', entidad_existente.destinatario if entidad_existente else '')
        estado_envio = dto.get('estado_envio', entidad_existente.estado_envio if entidad_existente else 'pendiente')
        
        if not mensaje or not destinatario:
            raise ValueError("mensaje y destinatario son obligatorios")

        return Notificacion(
            id=id_notificacion,
            mensaje=mensaje,
            destinatario=destinatario,
            estado_envio=estado_envio
        )
    
    def entidad_a_dto(self, entidad: Notificacion) -> dict:
        """
        Convierte una entidad Notificacion en un diccionario para enviarlo en la respuesta.
        """

        return {
            'id': str(entidad.id),
            'mensaje': entidad.mensaje,
            'destinatario': entidad.destinatario,
            'estado_envio': entidad.estado_envio
        }
    
    def externo_a_dto(self, externo: dict, entidad_existente=None) -> Notificacion:
        notificacion = self.dto_a_entidad(externo, entidad_existente)


