import sqlite3


DATABASE = "voxura.db"


def conectar():

    return sqlite3.connect(DATABASE)



def crear_tabla():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interesadas (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        nombre TEXT,

        edad TEXT,

        ubicacion TEXT,

        motivacion TEXT,

        telegram TEXT,

        fecha DATETIME DEFAULT CURRENT_TIMESTAMP

    )
    """)


    conexion.commit()

    conexion.close()



def guardar_interesada(
    nombre,
    edad,
    ubicacion,
    motivacion,
    telegram
):

    conexion = conectar()

    cursor = conexion.cursor()


    cursor.execute("""
    INSERT INTO interesadas
    (
    nombre,
    edad,
    ubicacion,
    motivacion,
    telegram
    )

    VALUES (?, ?, ?, ?, ?)

    """,
    (
    nombre,
    edad,
    ubicacion,
    motivacion,
    telegram
    ))


    conexion.commit()

    conexion.close()
