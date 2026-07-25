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

        telegram_id TEXT UNIQUE,

        username TEXT,

        nombre TEXT,

        edad TEXT,

        ubicacion TEXT,

        motivacion TEXT,

        estado TEXT DEFAULT 'en_proceso',

        fecha DATETIME DEFAULT CURRENT_TIMESTAMP

    )
    """)


    conexion.commit()
    conexion.close()



def crear_usuario(
    telegram_id,
    username
):

    conexion = conectar()
    cursor = conexion.cursor()


    cursor.execute("""
    INSERT OR IGNORE INTO interesadas
    (
        telegram_id,
        username
    )

    VALUES (?, ?)

    """,
    (
        telegram_id,
        username
    ))


    conexion.commit()
    conexion.close()



def actualizar_dato(
    telegram_id,
    campo,
    valor
):

    conexion = conectar()
    cursor = conexion.cursor()


    campos_permitidos = [
        "nombre",
        "edad",
        "ubicacion",
        "motivacion",
        "estado"
    ]


    if campo not in campos_permitidos:
        return


    cursor.execute(
        f"""
        UPDATE interesadas
        SET {campo}=?
        WHERE telegram_id=?
        """,
        (
            valor,
            telegram_id
        )
    )


    conexion.commit()
    conexion.close()



def obtener_usuario(
    telegram_id
):

    conexion = conectar()
    cursor = conexion.cursor()


    cursor.execute(
        """
        SELECT *
        FROM interesadas
        WHERE telegram_id=?
        """,
        (telegram_id,)
    )


    usuario = cursor.fetchone()

    conexion.close()


    return usuario
