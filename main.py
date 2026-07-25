from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    Application,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters
)

import os

from config import (
    TOKEN,
    ANGIE_ID,
    ANGIE_USERNAME,
    CANAL_CAPACITACION,
    CANAL_CONVIVENCIA
)

from database import (
    crear_tabla,
    crear_chica,
    actualizar,
    obtener
)

from messages import (
    BIENVENIDA,
    NOMBRE,
    EDAD,
    PAIS,
    MOTIVACION
)


# --------------------------
# Crear ficha para Angie
# --------------------------

def ficha(datos):

    return f"""
💙 NUEVA INTERESADA VOXURA

👤 Nombre:
{datos[2]}

🎂 Edad:
{datos[3]}

🌎 País:
{datos[4]}

✨ Motivación:
{datos[5]}

📲 Telegram:
@{datos[1] if datos[1] else "sin usuario"}
"""


# --------------------------
# Inicio automático
# --------------------------

async def iniciar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    usuario = update.effective_user

    crear_chica(
        usuario.id,
        usuario.username
    )

    await update.message.reply_text(
        BIENVENIDA,
        reply_markup=ReplyKeyboardMarkup(
            [
                [
                    KeyboardButton("✨ Quiero información")
                ]
            ],
            resize_keyboard=True
        )
    )



# --------------------------
# Manejo de mensajes
# --------------------------

async def mensajes(update: Update, context: ContextTypes.DEFAULT_TYPE):

    usuario = update.effective_user
    texto = update.message.text

    datos = obtener(usuario.id)


    # Si es nueva persona

    if not datos:

        crear_chica(
            usuario.id,
            usuario.username
        )

        await update.message.reply_text(
            BIENVENIDA,
            reply_markup=ReplyKeyboardMarkup(
                [
                    [
                        KeyboardButton(
                            "✨ Quiero información"
                        )
                    ]
                ],
                resize_keyboard=True
            )
        )

        return



    paso = datos[6]



    # Botón inicial

    if texto == "✨ Quiero información":

        actualizar(
            usuario.id,
            "paso",
            "nombre"
        )

        await update.message.reply_text(
            NOMBRE
        )

        return



    # Nombre

    if paso == "nombre":

        actualizar(
            usuario.id,
            "nombre",
            texto
        )

        actualizar(
            usuario.id,
            "paso",
            "edad"
        )

        await update.message.reply_text(
            EDAD
        )

        return



    # Edad

    if paso == "edad":

        actualizar(
            usuario.id,
            "edad",
            texto
        )

        actualizar(
            usuario.id,
            "paso",
            "pais"
        )

        await update.message.reply_text(
            PAIS
        )

        return



    # País

    if paso == "pais":

        actualizar(
            usuario.id,
            "pais",
            texto
        )

        actualizar(
            usuario.id,
            "paso",
            "motivacion"
        )

        await update.message.reply_text(
            MOTIVACION
        )

        return



    # Motivación

    if paso == "motivacion":

        actualizar(
            usuario.id,
            "motivacion",
            texto
        )

        actualizar(
            usuario.id,
            "paso",
            "completo"
        )


        datos = obtener(usuario.id)


        # Enviar ficha a Angie

        await context.bot.send_message(
            chat_id=ANGIE_ID,
            text=ficha(datos)
        )


        botones = ReplyKeyboardMarkup(
            [
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
            ],
            resize_keyboard=True
        )


        await update.message.reply_text(
            f"""
Gracias por compartir conmigo, {datos[2]} 💙✨

Ya envié tu información a Angie, nuestra líder de Voxura.

Mientras ella se comunica contigo puedes conocer más sobre nuestra comunidad.

Tu voz, tu esencia, tu oportunidad 💙
""",
            reply_markup=botones
        )

        return



    # Botones finales

    if texto == "👑 Hablar con Angie":

        await update.message.reply_text(
            f"""
Puedes escribirle directamente a Angie 💙

Telegram:
{ANGIE_USERNAME}
"""
        )


    elif texto == "📚 Capacitación":

        await update.message.reply_text(
            CANAL_CAPACITACION
        )


    elif texto == "💙 Comunidad":

        await update.message.reply_text(
            CANAL_CONVIVENCIA
        )



# --------------------------
# Ejecutar
# --------------------------

def main():

    crear_tabla()


    app = Application.builder().token(TOKEN).build()


    app.add_handler(
        CommandHandler(
            "start",
            iniciar
        )
    )


    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            mensajes
        )
    )


    print("Aura Voxura funcionando 💙")


    app.run_polling()



if __name__ == "__main__":
    main()
