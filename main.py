from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

import os

from config import (
    ANGIE_ID,
    ANGIE_USERNAME,
    CANAL_CAPACITACION,
    CANAL_CONVIVENCIA
)

from database import (
    crear_tabla,
    crear_usuario,
    actualizar_dato,
    obtener_usuario
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



# ----------------------------
# /start
# ----------------------------

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    usuario = update.effective_user


    crear_usuario(
        str(usuario.id),
        usuario.username
    )


    actualizar_dato(
        str(usuario.id),
        "estado",
        "nombre"
    )


    await update.message.reply_text(
        BIENVENIDA
    )


    await update.message.reply_text(
        PEDIR_NOMBRE
    )



# ----------------------------
# Manejo de respuestas
# ----------------------------

async def recibir_mensaje(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    usuario = update.effective_user

    telegram_id = str(usuario.id)

    texto = update.message.text



    datos = obtener_usuario(
        telegram_id
    )


    if not datos:

        crear_usuario(
            telegram_id,
            usuario.username
        )

        datos = obtener_usuario(
            telegram_id
        )



    estado = datos[7]



    # NOMBRE

    if estado == "nombre":

        actualizar_dato(
            telegram_id,
            "nombre",
            texto
        )


        actualizar_dato(
            telegram_id,
            "estado",
            "edad"
        )


        await update.message.reply_text(
            PEDIR_EDAD
        )


    # EDAD

    elif estado == "edad":

        actualizar_dato(
            telegram_id,
            "edad",
            texto
        )


        actualizar_dato(
            telegram_id,
            "estado",
            "ubicacion"
        )


        await update.message.reply_text(
            PEDIR_UBICACION
        )



    # UBICACION

    elif estado == "ubicacion":

        actualizar_dato(
            telegram_id,
            "ubicacion",
            texto
        )


        actualizar_dato(
            telegram_id,
            "estado",
            "motivacion"
        )


        await update.message.reply_text(
            PEDIR_MOTIVACION
        )



    # MOTIVACION

    elif estado == "motivacion":

        actualizar_dato(
            telegram_id,
            "motivacion",
            texto
        )


        actualizar_dato(
            telegram_id,
            "estado",
            "completado"
        )


        datos = obtener_usuario(
            telegram_id
        )


        ficha = crear_ficha(
            datos[4],
            datos[5],
            datos[6],
            datos[7],
            usuario.username
        )


        # ENVIAR FICHA A ANGIE

        await context.bot.send_message(
            chat_id=ANGIE_ID,
            text=ficha
        )



        botones = [
            [
                KeyboardButton(
                    "👑 Hablar con Angie"
                )
            ],
            [
                KeyboardButton(
                    "📚 Capacitación"
                )
            ],
            [
                KeyboardButton(
                    "💙 Comunidad"
                )
            ]
        ]


        teclado = ReplyKeyboardMarkup(
            botones,
            resize_keyboard=True
        )


        await update.message.reply_text(

            f"""
Gracias por compartir conmigo, {datos[4]} 💙✨

Ya envié tu información a Angie, nuestra líder de Voxura.

Mientras ella se comunica contigo puedes conocer más sobre nuestra comunidad y capacitación.

Tu voz, tu esencia, tu oportunidad 💙

""",

            reply_markup=teclado

        )



# ----------------------------
# Botones
# ----------------------------

async def botones(

    update: Update,

    context: ContextTypes.DEFAULT_TYPE

):

    texto = update.message.text



    if texto == "👑 Hablar con Angie":

        await update.message.reply_text(

            f"""
Puedes escribirle directamente a Angie 💙

Telegram:
{ANGIE_USERNAME}

Ella estará feliz de orientarte personalmente ✨

"""

        )



    elif texto == "📚 Capacitación":

        await update.message.reply_text(

            f"""
Aquí puedes entrar a nuestra capacitación inicial 💙

{CANAL_CAPACITACION}

"""

        )



    elif texto == "💙 Comunidad":

        await update.message.reply_text(

            f"""
Este es nuestro espacio de convivencia Voxura 💙

{CANAL_CONVIVENCIA}

"""

        )



# ----------------------------
# Ejecutar bot
# ----------------------------

def main():

    crear_tabla()


    app = Application.builder().token(TOKEN).build()



    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            botones
        )
    )


    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            recibir_mensaje
        )
    )



    print(
        "Aura Voxura activa 💙"
    )


    app.run_polling()



if __name__ == "__main__":

    main()
