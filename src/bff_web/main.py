from fastapi import FastAPI, Request
import asyncio
import uvicorn
from sse_starlette.sse import EventSourceResponse
from src.bff_web.api.v1.router import router as v1
from src.bff_web.consumidores import suscribirse_a_topico

app = FastAPI(title="BFF Procesador de Imágenes")
tasks = list()
eventos = list()

@app.on_event("startup")
async def app_startup():
    global tasks, eventos
    task = asyncio.ensure_future(suscribirse_a_topico("eventos.imagen", "procesador-bff", eventos=eventos))
    tasks.append(task)

@app.get('/stream')
async def stream_eventos(request: Request):
    async def leer_eventos():
        while True:
            if await request.is_disconnected():
                break
            if len(eventos) > 0:
                yield {'data': eventos.pop(), 'event': 'NuevoEvento'}
            await asyncio.sleep(0.1)

    return EventSourceResponse(leer_eventos())

app.include_router(v1, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, reload=True)
