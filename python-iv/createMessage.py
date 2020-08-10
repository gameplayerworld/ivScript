import json
import time
import datetime

class createMessage():
  iv = 0
  level = 0
  mode = 0

  def create(self,Sql,send,sleep,cfg,gmt):
    overview = ""
    i = 0
    new_pokemon = 0
    old_pokemon = 0
    id = 0

    now = datetime.datetime.now()
    print("####################==========\\ *** IV *** Update " + cfg.areaName + " " + now.strftime("%m/%d/%Y, %H:%M:%S") + " /==========####################\n")

    try:
      for encounter in Sql.encounter_id:
        name = self.getPokemon(Sql.pokemon_id[i],cfg.language)
        verify = " \u2705 " if not Sql.calc_endminsec[i] == None else " \u2754"
        angriff = Sql.individual_attack[i]
        verteidigung = Sql.individual_defense[i]
        leben = Sql.individual_stamina[i]
        iv = round(((angriff + verteidigung + leben ) / 45) *100)
        kurzattacke = self.getShortAttack(Sql.shortattack[i],cfg.language)
        ladeattacke = self.getLoadAttack(Sql.loadattack[i],cfg.language)
        cp_multiplier = Sql.cp_multiplier[i]
        level = self.getLevel(cp_multiplier)

        form = self.getForm(Sql.form[i],cfg.language)
        costume = self.getCostume(Sql.costume[i],cfg.language)

        mode = self.mode
        zeit = Sql.disappear_time[i]
        zeit = zeit + datetime.timedelta(hours=gmt)

        if form:
          getform = "(" + form + ")"
        else:
          getform = ""

        if costume:
          getcostume = "(" + costume + ")"
        else:
          getcostume = ""

        if(iv == 100):
          highlight = cfg.iv100 + " "
        elif(iv == 0):
          highlight = cfg.iv0 + " "
        else:
          highlight = ""

        if i == 0:
          poke = "\n<b>" + str(name) + str(getform) + str(getcostume) + ":</b>\n"
        else:
          if Sql.pokemon_id[i-1] != Sql.pokemon_id[i]:
            poke = "\n<b>" + str(name) + str(getform) + str(getcostume) + ":</b>\n"
          elif Sql.form[i-1] != Sql.form[i] or Sql.costume[i-1] != Sql.costume[i]:
            poke = "\n<b>" + str(name) + str(getform) + str(getcostume) + ":</b>\n"
          else:
            poke = ""          

        # Costum  bolt_line/normal_line
        bolt_line = str(highlight) + str(int(iv)) + "% " + str(name) + str(getform) + str(getcostume) + " " + self.getGeschlecht(Sql.gender[i]) + " (" + str(Sql.cp[i]) + ")" + str(zeit.strftime(" %H:%M:%S")) + verify
        normal_line = "L" + str(level) + " (" + str(angriff) + "/" + str(verteidigung) + "/" + str(leben) + ") " + str(kurzattacke) + "/" + str(ladeattacke)
        ###############################

        if send.list_output.__contains__(encounter):
          print("encounter_id: " + str(encounter) + " bereits gesendet")
          f = open(cfg.areaName+"output.txt", "r")
            # Split the string based on space delimiter 
          list_string = f.read()
          list_string = list_string[1:len(list_string)-1]
          f.close()
          list_string = list_string.split(', ') 
          id = list_string[send.list_output.index(encounter)]
          # Costum  Overview
          if cfg.sort_pokemon == True:
            overview += str(poke) + "<a href='" + cfg.ivchatUrl + "/" + str(id) + "'>" + str(highlight) + str(iv) + "% " + "L" + str(level) + " (" + str(angriff) +"/"+ str(verteidigung)+"/"+str(leben)+ ") " + str(Sql.cp[i]) + "WP</a>" + str(zeit.strftime(" %H:%M:%S")) + verify + "\n"
          else:
            overview += "<b>" + str(highlight) + str(iv) + "% " + str(name) + str(getform) + str(getcostume) + " " + str(Sql.cp[i]) + "WP, " + str(zeit.strftime(" %H:%M:%S")) + "</b>" + verify + "\n└ <a href='" + cfg.ivchatUrl + "/" + str(id) + "'>L" + str(level) + " (" + str(angriff) +"/"+ str(verteidigung)+"/"+str(leben)+ ") " + str(kurzattacke) + "/" + str(ladeattacke) +"</a>\n"
          new_pokemon +=1
          old_pokemon +=1
        else:
          if not mode:
            if ((iv >= self.iv or level >= self.level and not self.iv == 200) or iv > 0 and iv < 10 and cfg.nuller == True):
              id = send.send(bolt_line,normal_line,encounter,Sql.latitude[i],Sql.longitude[i])
              # Costum  Overview
              if cfg.sort_pokemon == True:
                overview += str(poke) + "<a href='" + cfg.ivchatUrl + "/" + str(id) + "'>" + str(highlight) + str(iv) + "% " + "L" + str(level) + " (" + str(angriff) +"/"+ str(verteidigung)+"/"+str(leben)+ ") " + str(Sql.cp[i]) + "WP</a>" + str(zeit.strftime(" %H:%M:%S")) + verify + "\n"
              else:
                overview += "<b>" + str(highlight) + str(iv) + "% " + str(name) + str(getform) + str(getcostume) + " " + str(Sql.cp[i]) + "WP, " + str(zeit.strftime(" %H:%M:%S")) + "</b>" + verify + "\n└ <a href='" + cfg.ivchatUrl + "/" + str(id) + "'>L" + str(level) + " (" + str(angriff) +"/"+ str(verteidigung)+"/"+str(leben)+ ") " + str(kurzattacke) + "/" + str(ladeattacke) +"</a>\n"
              new_pokemon +=1
          else:
            if ((iv >= self.iv and level >= self.level and not self.iv == 200) or iv > 0 and iv < 10 and cfg.nuller == True):
              id = send.send(bolt_line,normal_line,encounter,Sql.latitude[i],Sql.longitude[i])
              # Costum  Overview
              if cfg.sort_pokemon == True:
                overview += str(poke) + "<a href='" + cfg.ivchatUrl + "/" + str(id) + "'>" + str(highlight) + str(iv) + "% " + "L" + str(level) + " (" + str(angriff) +"/"+ str(verteidigung)+"/"+str(leben)+ ") " + str(Sql.cp[i]) + "WP</a>" + str(zeit.strftime(" %H:%M:%S")) + verify + "\n"
              else:
                overview += "<b>" + str(highlight) + str(iv) + "% " + str(name) + str(getform) + str(getcostume) + " " + str(Sql.cp[i]) + "WP, " + str(zeit.strftime(" %H:%M:%S")) + "</b>" + verify + "\n└ <a href='" + cfg.ivchatUrl + "/" + str(id) + "'>L" + str(level) + " (" + str(angriff) +"/"+ str(verteidigung)+"/"+str(leben)+ ") " + str(kurzattacke) + "/" + str(ladeattacke) +"</a>\n"
              new_pokemon +=1
        i +=1
      scanned = "\n" + self.getTranslate("from",cfg.language) + str(i) + self.getTranslate("scanned",cfg.language)
      send.sendOverview(overview,scanned,new_pokemon,old_pokemon)
      print("spawns: " + str(i))

    except Exception as e:
        outF = open(cfg.areaName+"error.txt","w")
        ausgabe = "Passierte in der CreateMessage.py\n"
        ausgabe += "encounter_id: " + str(Sql.encounter_id.__len__) + "\n"
        ausgabe += "calc_endminsec: " + str(Sql.calc_endminsec.__len__) + "\n"
        ausgabe += "pokemon_id: " + str(Sql.pokemon_id.__len__) + "\n"
        ausgabe += "individual_attack: " + str(Sql.individual_attack.__len__) + "\n"
        ausgabe += "individual_defense: " + str(Sql.individual_defense.__len__) + "\n"
        ausgabe += "individual_stamina: " + str(Sql.individual_stamina.__len__) + "\n"
        ausgabe += "disappear_time: " + str(Sql.disappear_time.__len__) + "\n"
        ausgabe += "cp: " + str(Sql.cp.__len__) + "\n"
        ausgabe += "cp_multiplier: " + str(Sql.cp_multiplier.__len__) + "\n"
        ausgabe += "shortattack: " + str(Sql.shortattack.__len__) + "\n"
        ausgabe += "loadattack: " + str(Sql.loadattack.__len__) + "\n"
        ausgabe += "gender: " + str(Sql.gender.__len__) + "\n"
        ausgabe += "longitude: " + str(Sql.longitude.__len__) + "\n"
        ausgabe += "latitude: " + str(Sql.latitude.__len__) + "\n"
        ausgabe += "Wert i = " + str(i) + "\n"
        outF.writelines(ausgabe + str(e))
        outF.close()

  ### get iv
  def getIV(self,value):
    f = open("iv-werte.txt", "r")
    list_string = f.read()
    list_string = list_string.split(',') 
    self.iv = int(list_string[value-1])  
    self.getLevel(value)  

  ### get level
  def getLeveFromFile(self,value):
    f = open("level-werte.txt", "r")
    list_string = f.read()
    list_string = list_string.split(',') 
    self.level = int(list_string[value-1])  

  ### get mode
  def getModeFromFile(self,value):
    f = open("mode-werte.txt","r")
    list_string = f.read()
    list_string = list_string.split(',') 
    self.mode = int(list_string[value-1])

  ### get pokemon name
  def getPokemon(self,value,language):
    data = open('json/Pokemon.json').read()
    switch = json.loads(data)
    self.getIV(value)
    self.getLeveFromFile(value)
    self.getModeFromFile(value)
    if not str(value) in switch:
      return switch["null"][language]
    else:
      return switch[str(value)][language]

  ### get pokemon form
  def getForm(self,value,language):
    data = open('json/Form.json').read()
    switch = json.loads(data)
    if not str(value) in switch:
      return switch["null"][language]
    else:
      return switch[str(value)][language]

  ### get pokemon costume
  def getCostume(self,value,language):
    data = open('json/Costume.json').read()
    switch = json.loads(data)
    if not str(value) in switch:
      return switch["null"][language]
    else:
      return switch[str(value)][language]

  ### get pokemon gender
  def getGeschlecht(self,value):
    if value == 1:
      return "\U00002642"
    elif value == 2:
      return "\U00002640"
    else:
      return "\U0000267E"
      
  ### get pokemon quick move
  def getShortAttack(self,value,language):
    data = open('json/ShortAttack.json').read()
    switch = json.loads(data)
    if not str(value) in switch:
      return switch["null"][language]
    else:
      return switch[str(value)][language]

  ### get pokemon load move
  def getLoadAttack(self,value,language):
    data = open('json/LoadAttack.json').read()
    switch = json.loads(data)
    if not str(value) in switch:
      return switch["null"][language]
    else:
      return switch[str(value)][language]

  ### get pokemon level
  def getLevel(self,value):
    switch = {
        0.094: 1,
        0.135137: 1.5,
        0.166398: 2,
        0.192650: 2.5,
        0.215732: 3,
        0.236572: 3.5,
        0.255720: 4,
        0.273530: 4.5,
        0.29025: 5,
        0.306057: 5.5,
        0.321088: 6,
        0.335445: 6.5,
        0.349213: 7,
        0.362457: 7.5,
        0.375236: 8,
        0.387592: 8.5,
        0.399567: 9,
        0.411193: 9.5,
        0.4225: 10,
        0.432926: 10.5,
        0.443108: 11,
        0.453059: 11.5,
        0.462798: 12,
        0.472336: 12.5,
        0.481685: 13,
        0.490855: 13.5,
        0.499858: 14,
        0.508701: 14.5,
        0.517394: 15,
        0.525942: 15.5,
        0.534354: 16,
        0.542635: 16.5,
        0.550793: 17,
        0.558830: 17.5,
        0.566755: 18,
        0.574569: 18.5,
        0.582279: 19,
        0.589887: 19.5,
        0.5974: 20,
        0.604823: 20.5,
        0.612157: 21,
        0.619404: 21.5,
        0.626567: 22,
        0.633649: 22.5,
        0.640653: 23,
        0.647580: 23.5,
        0.654436: 24,
        0.661219: 24.5,
        0.667934: 25,
        0.674581: 25.5,
        0.681165: 26,
        0.687684: 26.5,
        0.694144: 27,
        0.700542: 27.5,
        0.706884: 28,
        0.713169: 28.5,
        0.719399: 29,
        0.725575: 29.5,
        0.7317: 30,
        0.734741: 30.5,
        0.737769: 31,
        0.740785: 31.5,
        0.743789: 32,
        0.746781: 32.5,
        0.749761: 33,
        0.752729: 33.5,
        0.755686: 34,
        0.758630: 34.5,
        0.761564: 35
    }
    return switch.get(value,lambda: str(value))
    
  ### tranlate some other text
  def getTranslate(self,value,language):
    text = {
      "from": {
        "de": "(Von ",
        "en": "(of ",
        "fr": "(of "
      },
      "scanned": {
        "de": " aktiv gescannten Pok\u00E9mon)",
        "en": " actively scanned Pok\u00E9mon)",
        "fr": " actively scanned Pok\u00E9mon)"
      }
    }
    return text[value][language]