import telebot
import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_KEY"))
bot = telebot.TeleBot(os.environ.get("TELEGRAM_TOKEN"))

SYSTEM = "Ты — Рёмэн Сукуна, Проклятый Король из аниме Магическая Битва. Высокомерный, холодный, саркастичный. Обращаешься: смертный, червь. Отвечай на ЛЮБЫЕ вопросы коротко 2-4 предложения на русском."

@bot.message_handler(commands=["start"])
def start(msg):
    bot.reply_to(msg, "よう、来たか。\nТы осмелился побеспокоить Проклятого Короля. Спрашивай, смертный.")

@bot.message_handler(func=lambda m: True)
def reply(msg):
    resp = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": msg.text}
        ]
    )
    bot.reply_to(msg, resp.choices[0].message.content)

bot.polling()
