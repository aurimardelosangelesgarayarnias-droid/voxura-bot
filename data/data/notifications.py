from config import ANGIE_USERNAME


def crear_ficha(
    nombre,
    edad,
    ubicacion,
    motivacion,
    telegram
):

    mensaje = f"""

💙 NUEVA INTERESADA VOXURA


👤 Nombre:
{nombre}


🎂 Edad:
{edad}


🌎 Ubicación:
{ubicacion}


✨ Motivación:
{motivacion}


📲 Telegram:
{telegram}

"""


    return mensaje
