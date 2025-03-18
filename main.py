import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

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

bot.polling()
