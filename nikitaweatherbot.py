import telebot
import random
from telebot import types
import datetime
import pyowm

bot = telebot.TeleBot("")

owm = pyowm.OWM('5c5dcb9de33020f37192cd91e5f7c173', language='ru')

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('hello.tgs', 'rb')
	bot.send_sticker(message.chat.id, sti)
	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}. В этом боте в можете узнать погоду".format(message.from_user),parse_mode='html')

@bot.message_handler(content_types=['text'])
def lalala(message):
	place = message.text
	observation = owm.weather_at_place(place)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]
	answer = "В городе "+ place +" сейчас " + w.get_detailed_status() + "\n"
	answer += "Температура сейчас в районе " + str(round(temp)) + " градусов" + "\n\n"
	bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)