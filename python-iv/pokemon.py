import json

class pokemon():
  iv = 0
  level = 0
  mode = 0
  def getIV(self,value):
    f = open("iv-werte.txt", "r")
          # Split the string based on space delimiter 
    list_string = f.read()
    list_string = list_string.split(',') 
    self.iv = int(list_string[value-1])  
    self.getLevel(value)  

  def getLeveFromFile(self,value):
    f = open("level-werte.txt", "r")
          # Split the string based on space delimiter 
    list_string = f.read()
    list_string = list_string.split(',') 
    self.level = int(list_string[value-1])  

  def getModeFromFile(self,value):
    f = open("mode-werte.txt","r")
    list_string = f.read()
    list_string = list_string.split(',') 
    self.mode = int(list_string[value-1])  
    
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

  def getForm(self,value,language):
    data = open('json/Form.json').read()
    switch = json.loads(data)
    if not str(value) in switch:
      return switch["null"][language]
    else:
      return switch[str(value)][language]

  def getCostume(self,value,language):
    data = open('json/Costume.json').read()
    switch = json.loads(data)
    if not str(value) in switch:
      return switch["null"][language]
    else:
      return switch[str(value)][language]

  def getGeschlecht(self,value):
    if value == 1:
      return "\U00002642"
    elif value == 2:
      return "\U00002640"
    else:
      return "\U0000267E"

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