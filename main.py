from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

import os

from config import (
    CANAL_CAPACITACION,
    CANAL_CONVIVENCIA,
    ANGIE_USERNAME,
    ANGIE_ID
)

from database import (
    crear_tabla,
    guardar_interesada
)

from messages import (
    BIENVENIDA,
    PEDIR_NOMBRE,
    PEDIR_EDAD,
    PEDIR_UBICACION,
    PEDIR_MOTIVACION
)

from notifications import crear_ficha


TOKEN = os.getenv("BOT_TOKEN")


# Memoria temporal de usuarios
usuarios = {}



async def start(
