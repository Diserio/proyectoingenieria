from pony.orm import *
from starlette.routing import NoMatchFound
from pydantic import BaseModel

db = Database()

class Data(BaseModel):
    nombre : str
    def saludo(self):
        print("Hola Culia")

    
class Partida(db.Entity):
    id_partida = PrimaryKey(int, auto=True)
    nombre = Required(str, 20)
    iniciada = Optional(bool, default=False)
    jugadors = Set('Jugador')
    cantjugadores = Required(int, default=1)

class Jugador(db.Entity):
    id_jugador = PrimaryKey(int, auto=True)
    nombre = Required(str, 20, unique=True)
    color = Optional(str)
    partidas = Set(Partida)

@db_session
def nueva_partida(nombre: Data):
    partida = Partida(nombre = nombre.nombre, iniciada = False)
    commit()

    return partida

@db_session
def insertar_partidas():
    partidas = ["Partida 1", "Partida 2", "Partida 3"]
    for partida in partidas:
        Partida(nombre = partida, iniciada = False)

    commit()

@db_session
def devolver_partidas():
    partidas = list(select(p for p in Partida if not p.iniciada))
    return partidas


db.bind(provider = 'sqlite', filename = 'partidas.sqlite', create_db = True)
db.generate_mapping(create_tables = True)

if __name__ == "__main__":
    insertar_partidas()
    #mostrar_partidas()

    with db_session:
        p7 = Partida(nombre = "Partida 7", iniciada = True)
        commit()
        #for partida in devolver_partidas():
            #print(partida.nombre)

    #partidas = devolver_partidas()

    #for partida in partidas:
        #print(partida.to_dict())