#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser

####Hier wird die Config aus dem Configfile geladen und den einzelen
####Werten zugewiesen

class Config():
  host = ""
  database = ""
  user = ""
  password = ""
  token = ""
  language = ""
  sort_pokemon = bool
  sleepTime = ""
  iv100 = ""
  iv0 = ""

  def readConfig(self,cfgFile):  
    parser = ConfigParser()
    parser.read(cfgFile, encoding='utf-8')

    self.host = parser.get('Mysql', 'host')
    self.database = parser.get('Mysql', 'database')
    self.user = parser.get('Mysql', 'user')
    self.password = parser.get('Mysql', 'password')
    self.token = parser.get('Bot Settings', 'token')
    self.language = parser.get('Options', 'language')
    self.sort_pokemon = (parser.getboolean("Options", "sort_pokemon"))
    self.sleepTime = parser.get('Message', 'sleep_time')
    self.iv100 = parser.get('IV', '100')
    self.iv0 = parser.get('IV', '0')