from clients.seedwork.aplicacion.comandos import Comando, ComandoHandler

class AutenticarUsuario(Comando):
    email: str
    password: str

class AutenticarUsuarioHandler(ComandoHandler):
    ...