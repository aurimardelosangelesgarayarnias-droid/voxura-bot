from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

menu = ReplyKeyboardMarkup(
    [
        ["💜 Información"],
        ["💰 Ganancias"],
        ["📝 Registro"],
        ["👩‍💼 Contacto"]
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💜 Bienvenida a VOXURA 🪼\n\nSelecciona una opción:",
        reply_markup=menu
    )

async def mensajes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    if texto == "💜 Información":
        await update.message.reply_text(
            "VOXURA es una agencia que acompaña a streamers durante su crecimiento."
        )

    elif texto == "💰 Ganancias":
        await update.message.reply_text(
            "Las ganancias dependen de tu actividad y desempeño."
        )

    elif texto == "📝 Registro":
        await update.message.reply_text(
            "Por favor envía:\n\nNombre\nEdad\nPaís"
        )

    elif texto == "👩‍💼 Contacto":
        await update.message.reply_text(
            "Próximamente."
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, mensajes))

app.run_polling()
