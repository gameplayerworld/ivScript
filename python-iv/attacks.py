import json

class attacks():

  def getShortAttack(self,value,language):
    data = open('json/ShortAttack.json').read()
    switch = json.loads(data)
    return switch[str(value)][language]

  def getLoadAttack(self,value,language):
    data = open('json/LoadAttack.json').read()
    switch = json.loads(data)
    return switch[str(value)][language]