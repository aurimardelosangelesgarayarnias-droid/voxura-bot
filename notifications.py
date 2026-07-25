def crear_ficha(
    nombre,
    edad,
    ubicacion,
    motivacion,
    telegram
):

    return f"""

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
@{telegram if telegram else "Sin usuario"}

"""
