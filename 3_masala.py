import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

sportchilar = {
    "boks": {
        "bohodir jalolov": "Amerikalik bokschi, 3 marta og'ir vazn toifasida jahon chempioni.",
        "hasanboy": "Amerikalik bokschi, tarixdagi eng yosh og'ir vazn chempioni."
    },
    "kurash": {
        "Rustam Ampar": "O'zbekistonlik kurashchi, ko'plab xalqaro musobaqalarda g'olib bo'lgan.",
        "Kurt Angle": "Amerikalik kurashchi va professional kurashchi, Olimpiya chempioni."
    },
    "shaxmat": {
        "Garry Kasparov": "Shaxmat bo'yicha sobiq jahon chempioni, eng kuchli o'yinchilardan biri.",
        "Magnus Carlsen": "Norvegiyalik shaxmat bo'yicha jahon chempioni, shaxmat tarixidagi eng kuchli o'yinchilardan biri."
    }
}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Salom! Boks, kurash yoki shaxmat sportchilari haqida ma\'lumot olish uchun /sport tanlang.')

def sport(update: update, context: CallbackContext) -> None:
    update.message.reply_text('Iltimos, quyidagilardan birini tanlang:\n/boks\n/kurash\n/shaxmat')

def boks(update: Update, context: CallbackContext) -> None:
    msg = "\n".join([f"{name}: {info}" for name, info in sportchilar['boks'].items()])
    update.message.reply_text(f"Bokschilar:\n{msg}")

def kurash(update: Update, context: CallbackContext) -> None:
    msg = "\n".join([f"{name}: {info}" for name, info in sportchilar['kurash'].items()])
    update.message.reply_text(f"Kurashchilar:\n{msg}")

def shaxmat(update: Update, context: CallbackContext) -> None:
    msg = "\n".join([f"{name}: {info}" for name, info in sportchilar['shaxmat'].items()])
    update.message.reply_text(f"Shaxmatchilar:\n{msg}")

def main() -> None:
    updater = Updater("silka")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("sport", sport))
    dispatcher.add_handler(CommandHandler("boks", boks))
    dispatcher.add_handler(CommandHandler("kurash", kurash))
    dispatcher.add_handler(CommandHandler("shaxmat", shaxmat))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
