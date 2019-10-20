#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
import time
import telebot
from datetime import datetime
from configparser import ConfigParser

bot = telebot.TeleBot("744885487:AAFMkYEKj5NjaNEvQ_Fe9uRhB63y17itALw")


def split_string(string): 
  
    # Split the string based on space delimiter 
	list_string = string.split(',), (') 
      
	return list_string 



def run(host,database,user,password,token,chatId,sleepTime,ivStart):
	bot = telebot.TeleBot(token)
	lastMessageID = 0
	lastMessage = ""
	print("- - - - - - - - IV-Counter Script gestartet - - - - - - - -")
	while True:

		connection = MySQLdb.connect(host=host,db=database,user=user, passwd=password)
		cursor = connection.cursor()
	
		#Abfragen der Daten aus der Datenbank

		MySQLcounter = cursor.execute("SELECT individual_attack FROM pokemon where individual_attack >=0 AND timestampdiff(SECOND,disappear_time,NOW())<7200")
		counter = cursor.fetchall()
		counter = str(counter)

		MySQLperfekt = cursor.execute("SELECT count(*) FROM pokemon where individual_attack =15 AND individual_defense = 15 AND individual_stamina = 15")
		perfekt = cursor.fetchone()[0]
		perfekt = str(perfekt)

		#Verbindungsabbau zur MySQL-Datenbank
		cursor = cursor.close()
		connection.close()

		list_name = split_string(counter)
		run = len(list_name)
		zeit = datetime.now()
	
		message = "\U0001F50E IV-Werte um " + zeit.strftime("%H:%M") +  " \n\U0001F43E " + str(run) + " in 30 Minuten, \n\U0001F4AF " + str(perfekt) + " seit " + ivStart
		if message != lastMessage:
			try:
				id = bot.edit_message_text(message,chat_id=chatId, message_id=lastMessageID, parse_mode='HTML',disable_web_page_preview=True) ##Nachricht traunstein quests
			except:
				id = bot.send_message(chatId, message, parse_mode='HTML',disable_web_page_preview=True,disable_notification=True) ##Nachricht traunstein quests
				bot.pin_chat_message(chat_id=chatId, message_id=id.message_id,disable_notification=True)
			lastMessage = message
			lastMessageID = id.message_id
			time.sleep(int(sleepTime))

def init():
	parser = ConfigParser()
	parser.read('iv-config.ini', encoding='utf-8')

	host = parser.get('Mysql', 'host')
	database = parser.get('Mysql', 'database')
	user = parser.get('Mysql', 'user')
	password = parser.get('Mysql', 'password')

	sleepTime = parser.get('Message', 'sleep_time')
	ivStart = parser.get('Message', 'iv_start')

	token = parser.get('Bot Settings', 'token')
	chatId = parser.get('Bot Settings', 'chat_id')

	run(host,database,user,password,token,chatId,sleepTime,ivStart)
init()


