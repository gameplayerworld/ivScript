#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import datetime

class sendMessage():
  chatID = 0
  bot = ""
  list_output = [] ##Beinhaltet alle Encounters welche versendet wurden
  list_message_ID = []
  overview_old = ""
  overviewId = 0
  areaName = ""

  def send(self,bolt_line,normal_line,encounter,latitude,longitude):
    try: 
      id = self.bot.send_venue(self.ivchatID,latitude,longitude,bolt_line,normal_line,disable_notification=True)
      self.list_output.append(encounter)
      self.list_message_ID.append(id.message_id)
      outF = open(self.areaName+"output.txt","w")
      outF.writelines(str(self.list_message_ID))
      outF.close()
      return id.message_id
    except:
      print(self.areaName+" Venue Message konnte nicht versendet werden")
  
  def sendOverview(self,message,scanned,new_pokemon,old_pokemon):
    print("pokemon: " + str(new_pokemon))
    print("old pokemon: " + str(old_pokemon))
    if message == "":
      message = "Aktuell keine gefilterten Pokemon vorhanden\n"
    else:
      message+=scanned
    lengh = len(message) - len(self.overview_old)
    if not message == self.overview_old:
      # DEBUG:
      f = open("DEBUG.txt", "a")
      f.writelines("\n\n####################==========\\ " + str(datetime.datetime.now()) + " /==========####################")
      f.writelines("\n old Message len ==> " + str(len(self.overview_old)) + "\n")
      f.writelines(str(self.overview_old))
      f.writelines("\n new Message len ==> " + str(len(message)) + "\n")
      f.writelines(str(message))
      f.close()
      if (len(message) <= len(self.overview_old) and new_pokemon == old_pokemon) or (len(message) > len(self.overview_old) and lengh == 1):
        try:
          self.bot.edit_message_text(message,chat_id=self.chatID, message_id=self.overviewId.message_id, parse_mode='HTML',disable_web_page_preview=True) ##Nachricht 
          self.overview_old = message
        except:
          try:
            print(self.areaName+" Konnte aber nicht editiern")
            self.bot.delete_message(self.chatID,self.overviewId.message_id)
            self.overviewId = self.bot.send_message(self.chatID,message,parse_mode='HTML')
            self.overview_old = message
          except:
            print(self.areaName+" Overview Message konnte nicht editiert werden")    
      else:
        try: 
          self.bot.delete_message(self.chatID,self.overviewId.message_id)
          print("delete overview on " + str(datetime.datetime.now()))
          self.overviewId = self.bot.send_message(self.chatID,message,parse_mode='HTML')
          self.overview_old = message
        except:
          try:
            self.overviewId = self.bot.send_message(self.chatID,message,parse_mode='HTML',disable_web_page_preview=True,disable_notification=False)
            self.overview_old = message
          except:
            print(self.areaName+" Overview Message konnte nicht gesendet werden")
        finally:
          print("finsh at " + str(datetime.datetime.now()))
   
  def clearOutputList(self,encounter):
    i = 0
    print(self.areaName+" Checke Outputliste\n")
    for encount in self.list_output:
      if not encounter.__contains__(encount):
        try:
          print(self.areaName+" Entferne Nachricht")
          self.bot.delete_message(self.ivchatID,self.list_message_ID[i])
          self.list_message_ID.__delitem__(i)
          self.list_output.__delitem__(i)
        except:
          print(self.areaName+" Nachricht konnte nicht entfernt werden")
      i +=1
    outF = open(self.areaName+"output.txt","w")
    outF.writelines(str(self.list_message_ID))
    outF.close()

  def setConfig(self,token,ivchatID,chatID,areaName):
    self.areaName = areaName
    self.ivchatID = ivchatID
    self.chatID = chatID
    self.bot = telebot.TeleBot(token)
