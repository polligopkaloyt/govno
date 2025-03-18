from flask import Flask, request
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import threading

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
    play_button = InlineKeyboardButton("🎮 Играть", web_app={"url": "https://polligopkaloyt.github.io/creeper.github.io/"})
    
    # Кнопка "Информация"
    info_button = InlineKeyboardButton("ℹ Информация", callback_data="info")
    
    # Кнопка "Поддержка"
    support_button = InlineKeyboardButton("👥 Поддержка", url="https://t.me/C_T_P_A_XX")
    
    # Добавляем кнопки в разметку
    markup.add(play_button)
    markup.add(info_button, support_button)
    
    # Отправляем сообщение
    bot.send_message(message.chat.id, "привет! я крипер ^_^ и меня надо тапать!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "info")
def info_callback(call):
    bot.send_message(call.message.chat.id, "by: @HELLKYXX")

def start_bot():
    bot.remove_webhook()
    bot.set_webhook(url="https://govno-3gfn.onrender.com/" + TOKEN)
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=start_bot, daemon=True).start()
    app.run(host="0.0.0.0", port=10000)  # Открываем порт 10000
