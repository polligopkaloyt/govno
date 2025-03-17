import telebot
from flask import Flask, request

TOKEN = "7566708504:AAGfJ0IVUHQirgnePd3leIiG7M83hFGm5yc"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "OK", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://ТВОЙ_RAILWAY_URL/" + TOKEN)
    return "Webhook set!", 200

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "привет, я крипер и меня надо тапать йоу @HELLKYXX")

bot.polling()
