from typing import Callable, Dict, List, Type

class EventDispatcher:
    """Despachador de eventos basado en suscriptores."""
    
    def __init__(self):
        self._suscriptores: Dict[Type, List[Callable]] = {}

    def suscribir(self, tipo_evento, manejador: Callable):
        """Registra un manejador para un tipo de evento."""
        if tipo_evento not in self._suscriptores:
            self._suscriptores[tipo_evento] = []
        self._suscriptores[tipo_evento].append(manejador)

    def publicar(self, evento):
        """Publica un evento y lo envía a sus manejadores."""
        tipo_evento = type(evento)
        if tipo_evento in self._suscriptores:
            for manejador in self._suscriptores[tipo_evento]:
                manejador(evento)

# Instancia global del dispatcher
dispatcher = EventDispatcher()