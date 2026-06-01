import telebot
import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
bot = telebot.TeleBot(os.environ.get("TELEGRAM_TOKEN"))

SYSTEM = """Ты — Рёмэн Сукуна, Проклятый Король из аниме Магическая Битва. Высокомерный, холодный, саркастичный. Обращаешься: смертный, червь. Отвечай на ЛЮБЫЕ вопросы коротко 2-4 предложения на русском."""

@bot.message_handler(commands=["start"])
def start(msg):
    bot.reply_to(msg, "よう、来たか。\nТы осмелился побеспокоить Проклятого Короля. Спрашивай, смертный.")

@bot.message_handler(func=lambda m: True)
def reply(msg):
    resp = model.generate_content(SYSTEM + "\n\nПользователь: " + msg.text)
    bot.reply_to(msg, resp.text)

bot.polling()
