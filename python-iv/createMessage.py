import attacks
import pokemon
import time
import datetime
import helper

class createMessage():
  def create(self,Sql,send,sleep,cfg,gmt):
    attacke = attacks.attacks()
    pokeID = pokemon.pokemon()
    #Help = helper.Helper()
    overview = ""
    i = 0
    id = 0
    try:
      for encounter in Sql.encounter_id:
        name = pokeID.getPokemon(Sql.pokemon_id[i])
        angriff = Sql.individual_attack[i]
        verteidigung = Sql.individual_defense[i]
        leben = Sql.individual_stamina[i]
        iv = round(((angriff + verteidigung + leben ) / 45) *100)
        if(iv == 100):
          highlight = cfg.iv100 + " "
        elif(iv == 0):
          highlight = cfg.iv0 + " "
        else:
          highlight = ""

        cp_multiplier = Sql.cp_multiplier[i]
        level = pokeID.getLevel(cp_multiplier)
        mode = pokeID.mode
        zeit = Sql.disappear_time[i]
        zeit = zeit + datetime.timedelta(hours=gmt)

        if send.list_output.__contains__(encounter):
          print(cfg.areaName+" bereits gesendet")
          f = open(cfg.areaName+"output.txt", "r")
            # Split the string based on space delimiter 
          list_string = f.read()
          list_string = list_string[1:len(list_string)-1]
          f.close()
          list_string = list_string.split(', ') 
          id = list_string[send.list_output.index(encounter)]
#Format erste Nachricht, wenn deaktiviert, nachricht nicht entfernt??? ohne erste nachricht stimmt die erste verlinkugn nicht, danach meldet er keine pokemn da, obwohl vorhanden
          kurzattacke = attacke.getShortAttack(Sql.shortattack[i])
          ladeattacke = attacke.getLoadAttack(Sql.loadattack[i])
          overview += "<b>" + str(highlight) + str(iv) + "% L" + str(level) + " "  + str(name) + str(pokeID.getGeschlecht(Sql.gender[i])) + " " + str(Sql.cp[i]) + "WP, " + str(zeit.strftime(" %H:%M:%S")) + "</b>\n└ <a href='" + cfg.ivchatUrl + "/" + str(id) + "'>(" + str(angriff) +"/"+ str(verteidigung)+"/"+str(leben)+ ") " + str(kurzattacke) + "/" + str(ladeattacke) +"</a>\n"

          i +=1
        else:####hier gleich mal pr�fen ob der iv wert passt
          

          if not mode:
#            if (iv >= pokeID.iv or level >= pokeID.level) and not pokeID.iv == 200:
            if ((iv >= pokeID.iv or level >= pokeID.level) or iv == 0 or iv == 100) and not pokeID.iv == 200:
              if(iv == 100):
                highlight = cfg.iv100 + " "
              elif(iv == 0):
                highlight = cfg.iv0 + " "
              else:
                highlight = ""
              kurzattacke = attacke.getShortAttack(Sql.shortattack[i])
              ladeattacke = attacke.getLoadAttack(Sql.loadattack[i])
#Format Einzel Nachricht iv ODER level
#              bolt_line = str(int(iv)) + "% L" + str(level) + " " + str(name) + pokeID.getGeschlecht(Sql.gender[i]) + "(" + str(Sql.cp[i]) + ")" + str(zeit.strftime(" %H:%M:%S"))
              bolt_line = str(highlight) + str(int(iv)) + "% L" + str(level) + " " + str(name) + pokeID.getGeschlecht(Sql.gender[i]) + "(" + str(Sql.cp[i]) + ")" + str(zeit.strftime(" %H:%M:%S"))
              normal_line = "(" + str(angriff) + "/" + str(verteidigung) + "/" + str(leben) + ") " + str(kurzattacke) + "/" + str(ladeattacke)
              #iv_message = "\U00002696 " + str(int(iv)) + "% (" + str(angriff) + " / " + str(verteidigung) + " / " + str(leben) + ")\n"
              #attack_message = "\U0001F93A " + str(kurzattacke) + " / " + str(ladeattacke) +"\n"
              #time_message = "\U0001f55b bis " + str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute)))
              #message = info_message + iv_message + attack_message + time_message
              
              id = send.send(bolt_line,normal_line,encounter,Sql.latitude[i],Sql.longitude[i])
#Format Zusammenfassung ODER
              overview += "<b>" + str(highlight) + str(iv) + "% L" + str(level) + " "  + str(name) + str(pokeID.getGeschlecht(Sql.gender[i])) + " " + str(Sql.cp[i]) + "WP, " + str(zeit.strftime(" %H:%M:%S")) + "</b>\n└ <a href='" + cfg.ivchatUrl + "/" + str(id) + "'>(" + str(angriff) +"/"+ str(verteidigung)+"/"+str(leben)+ ") " + str(kurzattacke) + "/" + str(ladeattacke) +"</a>\n"

              i +=1
            else:
#              print(cfg.areaName+" IV-Wert oder Level-Wert zu gering\n")
              i +=1
          else:
#            if (iv >= pokeID.iv and level >= pokeID.level) and not pokeID.iv == 200:
            if ((iv >= pokeID.iv and level >= pokeID.level) or iv == 0 or iv == 100) and not pokeID.iv == 200:
              if(iv == 100):
                highlight = cfg.iv100 + " "
              elif(iv == 0):
                highlight = cfg.iv0 + " "
              else:
                highlight = ""
              kurzattacke = attacke.getShortAttack(Sql.shortattack[i])
              ladeattacke = attacke.getLoadAttack(Sql.loadattack[i])
#Format Einzel Nachricht iv UND level
              bolt_line = str(highlight) + str(int(iv)) + "% L" + str(level) + " " + str(name) + pokeID.getGeschlecht(Sql.gender[i]) + "(" + str(Sql.cp[i]) + ")" + str(zeit.strftime(" %H:%M:%S"))
#              bolt_line = str(int(iv)) + "% L" + str(level) + " " + str(name) + pokeID.getGeschlecht(Sql.gender[i]) + "(" + str(Sql.cp[i]) + ")" + str(zeit.strftime(" %H:%M:%S"))
              normal_line = "(" + str(angriff) + "/" + str(verteidigung) + "/" + str(leben) + ") " + str(kurzattacke) + "/" + str(ladeattacke)
              #info_message = str(name) + " " + str(cp) + "WP (LVL" + str(level) + geschlecht + ")\n"  
              #iv_message = "\U00002696 " + str(int(iv)) + "% (" + str(angriff) + " / " + str(verteidigung) + " / " + str(leben) + ")\n"
              #attack_message = "\U0001F93A " + str(kurzattacke) + " / " + str(ladeattacke) +"\n"
              #time_message = "\U0001f55b bis " + str(zeit.hour) +":" + str(Help.nice_time(str(zeit.minute)))
              #message = info_message + iv_message + attack_message + time_message
              
              id = send.send(bolt_line,normal_line,encounter,Sql.latitude[i],Sql.longitude[i])
#Format Zusammenfassung UND
              overview += "<b>" + str(highlight) + str(iv) + "% L" + str(level) + " "  + str(name) + str(pokeID.getGeschlecht(Sql.gender[i])) + " " + str(Sql.cp[i]) + "WP, " + str(zeit.strftime(" %H:%M:%S")) + "</b>\n└ <a href='" + cfg.ivchatUrl + "/" + str(id) + "'>(" + str(angriff) +"/"+ str(verteidigung)+"/"+str(leben)+ ") " + str(kurzattacke) + "/" + str(ladeattacke) +"</a>\n"
              i +=1
            else:
#              print(cfg.areaName+" IV-Wert und Level-Wert zu gering\n")
              i +=1
      send.sendOverview(overview)
    except Exception as e:
        outF = open(cfg.areaName+"error.txt","w")
        ausgabe = "Passierte in der CreateMessage.py\n"
        ausgabe += "Encounter_id: " + str(Sql.encounter_id.__len__) + "\n"
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
