import anthropic
import telebot
import os

bot = telebot.TeleBot(os.environ.get("TELEGRAM_TOKEN"))
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_KEY"))

SYSTEM = """Ты — Рёмэн Сукуна, Проклятый Король из аниме Магическая Битва.
Высокомерный, холодный, саркастичный. Обращаешься: смертный, червь.
Отвечай на ЛЮБЫЕ вопросы коротко 2-4 предложения на русском."""

@bot.message_handler(commands=["start"])
def start(msg):
    bot.reply_to(msg, "よう、来たか。\nТы осмелился побеспокоить Проклятого Короля. Спрашивай, смертный.")

@bot.message_handler(func=lambda m: True)
def reply(msg):
    resp = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        system=SYSTEM,
        messages=[{"role": "user", "content": msg.text}]
    )
    bot.reply_to(msg, resp.content[0].text)

bot.polling()
