import telebot
import os
from flask import Flask, request

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("Ошибка: Токен не найден в переменных окружения!")

bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Бот работает.")

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"https://govno-3gfn.onrender.com/{TOKEN}")
    app.run(host="44.227.217.144", port=5000)
