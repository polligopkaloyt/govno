from flask import Flask, request
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route("/")
def index():
    return "бот запущен"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@bot.message_handler(commands=["start"])
def start(message):
    markup = InlineKeyboardMarkup()
    
    # Кнопка "Играть"
    play_button = InlineKeyboardButton("🎮 играть", web_app={"url": "https://polligopkaloyt.github.io/creeper.github.io/"})
    
    # Кнопка "Информация"
    info_button = InlineKeyboardButton("ℹ информация", callback_data="info")
    
    # Кнопка "Поддержка"
    support_button = InlineKeyboardButton("👥 поддержка", url="https://t.me/C_T_P_A_XX")
    
    # Добавляем кнопки в разметку
    markup.add(play_button)
    markup.add(info_button, support_button)
    
    # Отправляем сообщение
    bot.send_message(message.chat.id, "привет! я крипер ^_^ и меня надо тапать!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "info")
def info_callback(call):
    bot.send_message(call.message.chat.id, "by: @HELLKYXX")

if __name__ == "__main__":
    bot.remove_webhook()  
    bot.set_webhook(url=f"https://govno-3gfn.onrender.com/{TOKEN}")  # Webhook без polling
    app.run(host="0.0.0.0", port=10000)  # Flask сервер на порту 10000
