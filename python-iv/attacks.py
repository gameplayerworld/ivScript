import json

class attacks():

  def getShortAttack(self,value,language):
    data = open('json/ShortAttack.json').read()
    switch = json.loads(data)
    if not str(value) in switch:
      return switch["null"][language]
    else:
      return switch[str(value)][language]

  def getLoadAttack(self,value,language):
    data = open('json/LoadAttack.json').read()
    switch = json.loads(data)
    if not str(value) in switch:
      return switch["null"][language]
    else:
      return switch[str(value)][language]