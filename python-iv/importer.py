import os
import requests

if not os.path.exists("json/"):
    os.mkdir("json/")
    print("json Directory Created ")
else:    
    print("json Directory already exists")

ShortAttack = 'https://raw.githubusercontent.com/Micha854/pogoProtos/master/shortAttacks.json'
r = requests.get(ShortAttack, allow_redirects=True)
open('json/ShortAttack.json', 'wb').write(r.content)

LoadAttack = 'https://raw.githubusercontent.com/Micha854/pogoProtos/master/LoadAttack.json'
r = requests.get(LoadAttack, allow_redirects=True)
open('json/LoadAttack.json', 'wb').write(r.content)

Pokemon = 'https://raw.githubusercontent.com/Micha854/pogoProtos/master/Pokemon.json'
r = requests.get(Pokemon, allow_redirects=True)
open('json/Pokemon.json', 'wb').write(r.content)

Form = 'https://raw.githubusercontent.com/Micha854/pogoProtos/master/Form.json'
r = requests.get(Form, allow_redirects=True)
open('json/Form.json', 'wb').write(r.content)

Costume = 'https://raw.githubusercontent.com/Micha854/pogoProtos/master/Costume.json'
r = requests.get(Costume, allow_redirects=True)
open('json/Costume.json', 'wb').write(r.content)