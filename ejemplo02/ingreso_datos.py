from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# ---------- Clubs ----------

# Abrimos el archivo datos_clubs.txt
archivo = open('data/datos_clubs.txt')

# Leemos las lineas del archivo
lineas = archivo.readlines()

# Separamos los datos y almacenamos en una lista
lista = [l.replace("\n", "").split(";") for l in lineas]

# Recorremos las lineas del archivo
for elemento in lista:
    club = Club(nombre = elemento[0], deporte = elemento[1], fundacion = elemento[2])
    session.add(club)

# Cerramos el archivo datos_clubs.txt que estamos leyendo
archivo.close()

# se confirma las transacciones
session.commit()


# ---------- Jugadores ----------

# Abrimos el archivo datos_jugadores.txt
archivo = open('data/datos_jugadores.txt')

# Leemos las lineas del archivo
lineas = archivo.readlines()

# Separamos los datos y almacenamos en una lista
lista = [l.replace("\n", "").split(";") for l in lineas]

# Recorremos las lineas del archivo
for elemento in lista:
    try:
        obj_club = session.query(Club).filter_by(nombre = elemento[0]).one()
        jugador = Jugador(nombre = elemento[3], dorsal = elemento[2], posicion = elemento[1], club = obj_club)
        session.add(jugador)
    except NoResultFound:
        print(None)

# Cerramos el archivo datos_jugadores.txt que estamos leyendo
archivo.close()

# se confirma las transacciones
session.commit()