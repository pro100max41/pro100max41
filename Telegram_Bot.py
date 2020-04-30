import telebot
import requests
import pyowm
from bs4 import BeautifulSoup as BS
from telebot import types



req=requests.get('https://minfin.com.ua/ua/currency/')

bot = telebot.TeleBot("1182619334:AAELfQ6hS5ELPtwmhEhOE_JcTEWApLAy5YQ")

owm= pyowm.OWM('485e527142b03cb2bfb32ae85f5794f4')

source= requests.get('https://minfin.com.ua/ua/currency/').text

soup=BS(source,'lxml')



html_code=soup.find('main')


value=html_code.find('span',class_='mfcur-nbu-full-wrap').text

sep="0"

value = value.split(sep, 1)[0]

#print(value)

try:
	@bot.message_handler(commands=['start'])
	def func_start(message):
		bot.send_message(message.chat.id,"Hello! I am Useful_bot. And I am going to help you.(for command list type: /help)")	
except:
	bot.send_message(message.chat.id,"You've entered wrong command. =(")	




try:
	@bot.message_handler(commands=['help'])
	def func_help(message):
		bot.send_message(message.chat.id,"The list of commands: \n /weather \n /currency ")	
except :
	bot.send_message(message.chat.id,"You've entered wrong command. =(")	


@bot.message_handler(commands=['weather'])
def func_weather(message):

	bot.send_message(message.chat.id,"Send me the name of your city! =)")

	print(message.text)

	@bot.message_handler(content_types=['text'])
	def get_place(message):


		
		city=message.text
	

		print(city)	
				
		try:
			observation= owm.weather_at_place(city)
			w=observation.get_weather()

			temp=w.get_temperature('celsius')['temp']	
			speed_wind=w.get_wind()['speed']

			reply1="The temperature of air is "+str(temp)+" in "+message.text+"\n"
			reply1+="The speed of wind is "+ str(speed_wind)+" in "+message.text+"\n"

			bot.send_message(message.chat.id,reply1)
		
		except:
			print("Crashed")
			bot.send_message(message.chat.id,"You've entered wrong city. Try again =(")	


@bot.message_handler(commands=['currency'])
def func_currency(message):
	print(message.text)
	print(value)
	bot.send_message(message.chat.id,f"Dollar: {value}")


	
bot.polling()
