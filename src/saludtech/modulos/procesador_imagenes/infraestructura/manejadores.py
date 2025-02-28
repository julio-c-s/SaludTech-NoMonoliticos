from saludtech.modulos.procesador_imagenes.dominio.eventos import (
    ImagenSubida, ImagenProcesada, ErrorProcesamientoImagen, ImagenEliminada, ImagenDescargada
)
from infraestructura.event_dispatcher import dispatcher

def manejar_imagen_subida(evento: ImagenSubida):
    print(f"📢 Imagen subida: ID {evento.imagen_id} | Usuario {evento.usuario_id} | Ruta {evento.ruta_archivo}")

def manejar_imagen_procesada(evento: ImagenProcesada):
    print(f"✅ Imagen procesada: ID {evento.imagen_id} | Formato {evento.formato_final} | Tamaño {evento.tamanio_final_kb} KB")

def manejar_error_procesamiento(evento: ErrorProcesamientoImagen):
    print(f"⚠️ Error procesando imagen: ID {evento.imagen_id} | Error: {evento.mensaje_error}")

def manejar_imagen_eliminada(evento: ImagenEliminada):
    print(f"🗑️ Imagen eliminada: ID {evento.imagen_id} | Usuario {evento.usuario_id} | Motivo: {evento.motivo}")

def manejar_imagen_descargada(evento: ImagenDescargada):
    print(f"⬇️ Imagen descargada: ID {evento.imagen_id} | Usuario {evento.usuario_id} | Formato: {evento.formato_descargado}")

# Suscribir los manejadores a los eventos
dispatcher.suscribir(ImagenSubida, manejar_imagen_subida)
dispatcher.suscribir(ImagenProcesada, manejar_imagen_procesada)
dispatcher.suscribir(ErrorProcesamientoImagen, manejar_error_procesamiento)
dispatcher.suscribir(ImagenEliminada, manejar_imagen_eliminada)
dispatcher.suscribir(ImagenDescargada, manejar_imagen_descargada)