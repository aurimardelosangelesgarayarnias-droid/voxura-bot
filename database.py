import sqlite3

DB = "voxura.db"


def conectar():
    return sqlite3.connect(DB)


def crear_tabla():

    con = conectar()
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS chicas(
        id INTEGER PRIMARY KEY,
        username TEXT,
        nombre TEXT,
        edad TEXT,
        pais TEXT,
        motivacion TEXT,
        paso TEXT
    )
    """)

    con.commit()
    con.close()



def crear_chica(user_id, username):

    con = conectar()
    cur = con.cursor()

    cur.execute("""
    INSERT OR IGNORE INTO chicas
    (id, username, paso)
    VALUES (?, ?, ?)
    """,
    (
        user_id,
        username,
        "nombre"
    ))

    con.commit()
    con.close()



def actualizar(user_id, campo, valor):

    con = conectar()
    cur = con.cursor()

    cur.execute(
        f"""
        UPDATE chicas
        SET {campo}=?
        WHERE id=?
        """,
        (
            valor,
            user_id
        )
    )

    con.commit()
    con.close()



def obtener(user_id):

    con = conectar()
    cur = con.cursor()

    cur.execute(
        """
        SELECT *
        FROM chicas
        WHERE id=?
        """,
        (user_id,)
    )

    data = cur.fetchone()

    con.close()

    return data



def borrar(user_id):

    con = conectar()
    cur = con.cursor()

    cur.execute(
        "DELETE FROM chicas WHERE id=?",
        (user_id,)
    )

    con.commit()
    con.close()
