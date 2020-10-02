#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import datetime
import json
import os
import sys
import matplotlib.path as mplPath
import numpy as np
from termcolor import colored

class sendMessage():
  chatID = 0
  bot = ""
  list_output = []
  overview_old = {}
  overviewId = 0
  clear = {}
  last_encounter_id = []
  isfile = 0

  # load areas with all your channels
  data = open('areas.json').read()
  switch = json.loads(data)
  
  for areas in switch['channels']:
    overview_old[areas['Name']] = ""
    if not os.path.exists(areas['Name']):
      os.mkdir(areas['Name'])
    if areas['Name'] not in clear:
      clear[areas['Name']] = {'encounter': [], 'messageID': [], 'listID': []}
    if not os.path.isfile(areas['Name']+"/iv-werte.txt"):
      print(colored("   ERROR:", 'red') + " file " + colored("iv-werte.txt", 'yellow') + " in folder " + colored(str(areas['Name']), 'yellow') + " does not exist!")
      isfile += 1
    if not os.path.isfile(areas['Name']+"/level-werte.txt"):
      print(colored("   ERROR:", 'red') + " file " + colored("level-werte.txt", 'yellow') + " in folder " + colored(str(areas['Name']), 'yellow') + " does not exist!")
      isfile += 1
    if not os.path.isfile(areas['Name']+"/mode-werte.txt"):
      print(colored("   ERROR:", 'red') + " file " + colored("mode-werte.txt", 'yellow') + " in folder " + colored(str(areas['Name']), 'yellow') + " does not exist!")
      isfile += 1
  
  if isfile:
    sys.exit(colored("    INFO:", 'cyan') + " Das Script wurde beendet, da " + str(isfile) + " Dateien fehlen!!!")

  # save clear.json
  def write_json(self, clear, filename='clear.json'):
    with open(filename, 'w') as data:
      json.dump(self.clear, data, indent=4)

  # send venue messages
  def send(self,bolt_line,normal_line,encounter,latitude,longitude,ChatName,ChatId):
    try:
      id = self.bot.send_venue(ChatId,latitude,longitude,bolt_line,normal_line,disable_notification=True)
      self.list_output.append(encounter)
      self.clear[ChatName]['messageID'].append(id.message_id)
      self.clear[ChatName]['encounter'].append(encounter)
      self.write_json(self.clear)
      print(colored(" SUCCESS:", 'green') + " Sende encounter " + str(encounter) + " in " + str(ChatName))
      return id.message_id
    except:
      print(colored("   ERROR:", 'red') + " encounter " + str(encounter) + " konnte nicht versendet werden")
  
  def sendOverview(self,message,scanned,new_pokemon,old_pokemon):
    for areas in self.switch['channels']:
      self.chatID = areas['chat_id']

      #print("OVERVIEW OF: " + areas['Name'])
      #print(message[areas['Name']])

      #print("\nOLD OVERVIEW OF: " + areas['Name'])
      #print(self.overview_old[areas['Name']])

      if message[areas['Name']] == "":
        message[areas['Name']] = "Aktuell keine gefilterten Pokemon vorhanden\n"
      else:
        message[areas['Name']]

      lengh = len(message[areas['Name']]) - len(self.overview_old[areas['Name']])

      if not message[areas['Name']] == self.overview_old[areas['Name']]:
        if (len(message[areas['Name']]) <= len(self.overview_old[areas['Name']]) and new_pokemon[areas['Name']] == old_pokemon[areas['Name']]) or (len(message[areas['Name']]) > len(self.overview_old[areas['Name']]) and lengh == 1):
          try:
            self.bot.edit_message_text(message[areas['Name']],chat_id=self.chatID, message_id=self.clear[areas['Name']]['listID'], parse_mode='HTML',disable_web_page_preview=True) ##Nachricht
            self.overview_old[areas['Name']] = message[areas['Name']]
            print(colored(" SUCCESS:", 'green') + " Overview in " + areas['Name'] + " wurde editiert")
          except:
            try:
              self.bot.delete_message(self.chatID,self.clear[areas['Name']]['listID'])
              self.overviewId = self.bot.send_message(self.chatID,message[areas['Name']],parse_mode='HTML')
              self.clear[areas['Name']]['listID'] = self.overviewId.message_id
              self.overview_old[areas['Name']] = message[areas['Name']]
              print(colored(" WARNING:", 'yellow') + " Overview in " + areas['Name'] + " konnte nicht editiert werden")
            except:
              print(colored("   ERROR:", 'red') + " Overview in " + areas['Name'] + " konnte nicht erneut gesendet werden")
        else:
          try: 
            self.bot.delete_message(self.chatID,self.clear[areas['Name']]['listID'])
            self.overviewId = self.bot.send_message(self.chatID,message[areas['Name']],parse_mode='HTML')
            self.clear[areas['Name']]['listID'] = self.overviewId.message_id
            self.overview_old[areas['Name']] = message[areas['Name']]
            print(colored(" SUCCESS:", 'green') + " Overview in " + areas['Name'] + " wurde Neu gesendet")
          except:
            try:
              self.overviewId = self.bot.send_message(self.chatID,message[areas['Name']],parse_mode='HTML',disable_web_page_preview=True,disable_notification=False)
              self.clear[areas['Name']]['listID'] = self.overviewId.message_id
              self.overview_old[areas['Name']] = message[areas['Name']]
              print(colored(" SUCCESS:", 'green') + " Overview in " + areas['Name'] + " wurde gesendet")
            except:
              print(colored("   ERROR:", 'red') + " Overview in " + areas['Name'] + " konnte nicht gesendet werden")
        self.write_json(self.clear)
   
  def clearOutputList(self,encounter):
    i = 0
    now = datetime.datetime.now()
    print(colored("    INFO:", 'cyan') + " Checke Outputliste " + now.strftime("%H:%M:%S") + ", Total Spawns " + str(len(self.last_encounter_id)) + " (" + str(len(self.list_output)) + " gemeldet)")

    for areas in self.switch['channels']:
      for encount in self.clear[areas['Name']]['encounter']:
        index = self.clear[areas['Name']]['encounter'].index(encount)
        if not encounter.__contains__(encount):
          try:
            self.bot.delete_message(areas['ivchat_id'],self.clear[areas['Name']]['messageID'][index])
            self.clear[areas['Name']]['messageID'].__delitem__(index)
            self.clear[areas['Name']]['encounter'].__delitem__(index)
            self.list_output.remove(encount)
            print(colored(" SUCCESS:", 'green') + " Entferne encounter " + str(encount) + " in " + areas['Name'])
          except:
            print(colored("   ERROR:", 'red') + " encounter " + str(encount) + " in " + areas['Name'] + " konnte nicht entfernt werden")
        i +=1

      self.write_json(self.clear)

  def setConfig(self,token):
    self.bot = telebot.TeleBot(token)