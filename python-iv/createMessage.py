import attacks
import pokemon
import time
import datetime

class createMessage():
  def create(self,Sql,send,sleep,cfg,gmt):
    attacke = attacks.attacks()
    pokeID = pokemon.pokemon()
    overview = ""
    i = 0
    id = 0

    now = datetime.datetime.now()
    print("####################==========\\ *** IV *** Update " + cfg.areaName + " " + now.strftime("%m/%d/%Y, %H:%M:%S") + " /==========####################\n")
    print(Sql.form)


    try:
      for encounter in Sql.encounter_id:
        name = pokeID.getPokemon(Sql.pokemon_id[i],cfg.language)
        verify = " \u2705 " if not Sql.calc_endminsec[i] == None else " \u2754"
        angriff = Sql.individual_attack[i]
        verteidigung = Sql.individual_defense[i]
        leben = Sql.individual_stamina[i]
        iv = round(((angriff + verteidigung + leben ) / 45) *100)
        kurzattacke = attacke.getShortAttack(Sql.shortattack[i],cfg.language)
        ladeattacke = attacke.getLoadAttack(Sql.loadattack[i],cfg.language)
        cp_multiplier = Sql.cp_multiplier[i]
        level = pokeID.getLevel(cp_multiplier)

        form = pokeID.getForm(Sql.form[i],cfg.language)
        costume = pokeID.getCostume(Sql.costume[i],cfg.language)

        mode = pokeID.mode
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

        # Costum  bolt_line/normal_line
        bolt_line = str(highlight) + str(int(iv)) + "% " + str(name) + str(getform) + str(getcostume) + " " + pokeID.getGeschlecht(Sql.gender[i]) + " (" + str(Sql.cp[i]) + ")" + str(zeit.strftime(" %H:%M:%S")) + verify
        normal_line = "(L" + str(level) + ", " + str(angriff) + "/" + str(verteidigung) + "/" + str(leben) + ") " + str(kurzattacke) + "/" + str(ladeattacke)
        ###############################

        if send.list_output.__contains__(encounter):
          print(cfg.areaName+" bereits gesendet")
          f = open(cfg.areaName+"output.txt", "r")
            # Split the string based on space delimiter 
          list_string = f.read()
          list_string = list_string[1:len(list_string)-1]
          f.close()
          list_string = list_string.split(', ') 
          id = list_string[send.list_output.index(encounter)]
          # Costum  Overview
          overview += "<b>" + str(highlight) + str(iv) + "% " + str(name) + str(getform) + str(getcostume) + " " + str(pokeID.getGeschlecht(Sql.gender[i])) + " " + str(Sql.cp[i]) + "WP, " + str(zeit.strftime(" %H:%M:%S")) + "</b>" + verify + "\n└ <a href='" + cfg.ivchatUrl + "/" + str(id) + "'>(L" + str(level) + ", " + str(angriff) +"/"+ str(verteidigung)+"/"+str(leben)+ ") " + str(kurzattacke) + "/" + str(ladeattacke) +"</a>\n"
        else:
          if not mode:
            if ((iv >= pokeID.iv or level >= pokeID.level) or iv == 0 or iv == 100) and not pokeID.iv == 200:
              id = send.send(bolt_line,normal_line,encounter,Sql.latitude[i],Sql.longitude[i])
              # Costum  Overview
              overview += "<b>" + str(highlight) + str(iv) + "% " + str(name) + str(getform) + str(getcostume) + " " + str(pokeID.getGeschlecht(Sql.gender[i])) + " " + str(Sql.cp[i]) + "WP, " + str(zeit.strftime(" %H:%M:%S")) + "</b>" + verify + "\n└ <a href='" + cfg.ivchatUrl + "/" + str(id) + "'>(L" + str(level) + ", " + str(angriff) +"/"+ str(verteidigung)+"/"+str(leben)+ ") " + str(kurzattacke) + "/" + str(ladeattacke) +"</a>\n"
          else:
            if ((iv >= pokeID.iv and level >= pokeID.level) or iv == 0 or iv == 100) and not pokeID.iv == 200:
              id = send.send(bolt_line,normal_line,encounter,Sql.latitude[i],Sql.longitude[i])
              # Costum  Overview
              overview += "<b>" + str(highlight) + str(iv) + "% " + str(name) + str(getform) + str(getcostume) + " " + str(pokeID.getGeschlecht(Sql.gender[i])) + " " + str(Sql.cp[i]) + "WP, " + str(zeit.strftime(" %H:%M:%S")) + "</b>" + verify + "\n└ <a href='" + cfg.ivchatUrl + "/" + str(id) + "'>(L" + str(level) + ", " + str(angriff) +"/"+ str(verteidigung)+"/"+str(leben)+ ") " + str(kurzattacke) + "/" + str(ladeattacke) +"</a>\n"
        i +=1
      scanned = "\n" + self.getTranslate("from",cfg.language) + str(i) + self.getTranslate("scanned",cfg.language)
      send.sendOverview(overview,scanned)
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