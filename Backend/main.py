from fastapi import FastAPI
from models import devolver_partidas, nueva_partida, Data

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/nueva-partida/")
async def crear_partida(nombre: Data):
    partida = nueva_partida(nombre)
    new_id = partida.id_partida
    partnombre = partida.nombre
    print(type (new_id))
    nombre.saludo()
    return (new_id,partnombre)

@app.get("/partidas/")
def listar_partidas():
    partidas = devolver_partidas()

    return [p.nombre for p in partidas]