import MySQLdb
import time

class Sql():
  encounter_id = []
  pokemon_id = []
  individual_attack = []
  individual_defense = []
  individual_stamina = []
  disappear_time = []
  cp = []
  cp_multiplier = []
  shortattack = []
  loadattack = []
  gender = []
  longitude = []
  latitude = []

  def startSQL(self,cfg,modul):
    #Verbindungsaufbau zur MySQL-Datenbank
    try:
      connection = MySQLdb.connect(host=cfg.host,db=cfg.database,user=cfg.user, passwd=cfg.password)
      cursor = connection.cursor()
    except:
      print("Kein Verbindungsaufbau zur Datenbank, probiere es in 15 Sekunden erneut\n")
      time.sleep(15)
      return self.startSQL(cfg,modul)
    self.encounter_id.clear()
    self.pokemon_id.clear()
    self.individual_attack.clear()
    self.individual_defense.clear()
    self.individual_stamina.clear()
    self.disappear_time.clear()
    self.cp.clear()
    self.cp_multiplier.clear()
    self.shortattack.clear()
    self.loadattack.clear()
    self.gender.clear()
    self.longitude.clear()
    self.latitude.clear()

#Abfragen der Daten aus der Datenbank
    if modul == "0er":

      MySQLall = cursor.execute("SELECT encounter_id,pokemon_id,individual_attack,individual_defense,individual_stamina,disappear_time,cp,cp_multiplier,move_1,move_2,gender,longitude,latitude FROM pokemon where individual_attack IS NOT NULL AND disappear_time > utc_timestamp() AND longitude BETWEEN " + cfg.min_longitude + " AND " + cfg.max_longitude + " AND latitude BETWEEN " + cfg.min_latitude + " AND " + cfg.max_latitude + " ORDER BY round(((`individual_attack` + `individual_defense` + `individual_stamina` ) / 45) *100) DESC, disappear_time DESC")
      all = cursor.fetchall()
      i = 0
      try:
        while i < len(all):
          self.encounter_id.append(all[i][0])
          self.pokemon_id.append(all[i][1])
          self.individual_attack.append(all[i][2])
          self.individual_defense.append(all[i][3])
          self.individual_stamina.append(all[i][4])
          self.disappear_time.append(all[i][5])
          self.cp.append(all[i][6])
          self.cp_multiplier.append(all[i][7])
          self.shortattack.append(all[i][8])
          self.loadattack.append(all[i][9])
          self.gender.append(all[i][10])
          self.longitude.append(all[i][11])
          self.latitude.append(all[i][12])
          i +=1
      except Exception as e:
        outF = open(self.areaName+"error.txt","w")
        ausgabe = "Passierte in der SQL.py\n"
        ausgabe += "Encounter_id: " + str(self.encounter_id.__len__) + "\n"
        ausgabe += "pokemon_id: " + str(self.pokemon_id.__len__) + "\n"
        ausgabe += "individual_attack: " + str(self.individual_attack.__len__) + "\n"
        ausgabe += "individual_defense: " + str(self.individual_defense.__len__) + "\n"
        ausgabe += "individual_stamina: " + str(self.individual_stamina.__len__) + "\n"
        ausgabe += "disappear_time: " + str(self.disappear_time.__len__) + "\n"
        ausgabe += "cp: " + str(self.cp.__len__) + "\n"
        ausgabe += "cp_multiplier: " + str(self.cp_multiplier.__len__) + "\n"
        ausgabe += "shortattack: " + str(self.shortattack.__len__) + "\n"
        ausgabe += "loadattack: " + str(self.loadattack.__len__) + "\n"
        ausgabe += "gender: " + str(self.gender.__len__) + "\n"
        ausgabe += "longitude: " + str(self.longitude.__len__) + "\n"
        ausgabe += "latitude: " + str(self.latitude.__len__) + "\n"
        ausgabe += "Wert i" + str(i) + "\n"
        ausgabe += "All Variable: " + str(len(all))
        outF.writelines(ausgabe + str(e))
        outF.close()


      
    cursor = cursor.close()
    connection.close()
