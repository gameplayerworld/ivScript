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
    switch = {
      1: {
        "de": "Bisasam",
        "en": "Bulbasaur",
        "fr": "Bulbizarre"
      },
      2: {
        "de": "Bisaknosp",
        "en": "Ivysaur",
        "fr": "Herbizarre"
      },
      3: {
        "de": "Bisaflor",
        "en": "Venusaur",
        "fr": "Florizarre"
      },
      4: {
        "de": "Glumanda",
        "en": "Charmander",
        "fr": "Salamèche"
      },
      5: {
        "de": "Glutexo",
        "en": "Charmeleon",
        "fr": "Reptincel"
      },
      6: {
        "de": "Glurak",
        "en": "Charizard",
        "fr": "Dracaufeu"
      },
      7: {
        "de": "Schiggy",
        "en": "Squirtle",
        "fr": "Carapuce"
      },
      8: {
        "de": "Schillok",
        "en": "Wartortle",
        "fr": "Carabaffe"
      },
      9: {
        "de": "Turtok",
        "en": "Blastoise",
        "fr": "Tortank"
      },
      10: {
        "de": "Raupy",
        "en": "Caterpie",
        "fr": "Chenipan"
      },
      11: {
        "de": "Safcon",
        "en": "Metapod",
        "fr": "Chrysacier"
      },
      12: {
        "de": "Smettbo",
        "en": "Butterfree",
        "fr": "Papilusion"
      },
      13: {
        "de": "Hornliu",
        "en": "Weedle",
        "fr": "Aspicot"
      },
      14: {
        "de": "Kokuna",
        "en": "Kakuna",
        "fr": "Coconfort"
      },
      15: {
        "de": "Bibor",
        "en": "Beedrill",
        "fr": "Dardargnan"
      },
      16: {
        "de": "Taubsi",
        "en": "Pidgey",
        "fr": "Roucool"
      },
      17: {
        "de": "Tauboga",
        "en": "Pidgeotto",
        "fr": "Roucoups"
      },
      18: {
        "de": "Tauboss",
        "en": "Pidgeot",
        "fr": "Roucarnage"
      },
      19: {
        "de": "Rattfratz",
        "en": "Rattata",
        "fr": "Rattata"
      },
      20: {
        "de": "Rattikarl",
        "en": "Raticate",
        "fr": "Rattatac"
      },
      21: {
        "de": "Habitak",
        "en": "Spearow",
        "fr": "Piafabec"
      },
      22: {
        "de": "Ibitak",
        "en": "Fearow",
        "fr": "Rapasdepic"
      },
      23: {
        "de": "Rettan",
        "en": "Ekans",
        "fr": "Abo"
      },
      24: {
        "de": "Arbok",
        "en": "Arbok",
        "fr": "Arbok"
      },
      25: {
        "de": "Pikachu",
        "en": "Pikachu",
        "fr": "Pikachu"
      },
      26: {
        "de": "Raichu",
        "en": "Raichu",
        "fr": "Raichu"
      },
      27: {
        "de": "Sandan",
        "en": "Sandshrew",
        "fr": "Sabelette"
      },
      28: {
        "de": "Sandamer",
        "en": "Sandslash",
        "fr": "Sablaireau"
      },
      29: {
        "de": "Nidoran♀",
        "en": "Nidoran♀",
        "fr": "Nidoran♀"
      },
      30: {
        "de": "Nidorina",
        "en": "Nidorina",
        "fr": "Nidorina"
      },
      31: {
        "de": "Nidoqueen",
        "en": "Nidoqueen",
        "fr": "Nidoqueen"
      },
      32: {
        "de": "Nidoran♂",
        "en": "Nidoran♂",
        "fr": "Nidoran♂"
      },
      33: {
        "de": "Nidorino",
        "en": "Nidorino",
        "fr": "Nidorino"
      },
      34: {
        "de": "Nidoking",
        "en": "Nidoking",
        "fr": "Nidoking"
      },
      35: {
        "de": "Piepi",
        "en": "Clefairy",
        "fr": "Mélofée"
      },
      36: {
        "de": "Pixi",
        "en": "Clefable",
        "fr": "Mélodelfe"
      },
      37: {
        "de": "Vulpix",
        "en": "Vulpix",
        "fr": "Goupix"
      },
      38: {
        "de": "Vulnona",
        "en": "Ninetales",
        "fr": "Feunard"
      },
      39: {
        "de": "Pummeluff",
        "en": "Jigglypuff",
        "fr": "Rondoudou"
      },
      40: {
        "de": "Knuddeluff",
        "en": "Wigglytuff",
        "fr": "Grodoudou"
      },
      41: {
        "de": "Zubat",
        "en": "Zubat",
        "fr": "Nosferapti"
      },
      42: {
        "de": "Golbat",
        "en": "Golbat",
        "fr": "Nosferalto"
      },
      43: {
        "de": "Myrapla",
        "en": "Oddish",
        "fr": "Mystherbe"
      },
      44: {
        "de": "Duflor",
        "en": "Gloom",
        "fr": "Ortide"
      },
      45: {
        "de": "Giflor",
        "en": "Vileplume",
        "fr": "Rafflesia"
      },
      46: {
        "de": "Paras",
        "en": "Paras",
        "fr": "Paras"
      },
      47: {
        "de": "Parasek",
        "en": "Parasect",
        "fr": "Parasect"
      },
      48: {
        "de": "Bluzuk",
        "en": "Venonat",
        "fr": "Mimitoss"
      },
      49: {
        "de": "Omot",
        "en": "Venomoth",
        "fr": "Aéromite"
      },
      50: {
        "de": "Digda",
        "en": "Diglett",
        "fr": "Taupiqueur"
      },
      51: {
        "de": "Digdri",
        "en": "Dugtrio",
        "fr": "Triopikeur"
      },
      52: {
        "de": "Mauzi",
        "en": "Meowth",
        "fr": "Miaouss"
      },
      53: {
        "de": "Snobilikat",
        "en": "Persian",
        "fr": "Persian"
      },
      54: {
        "de": "Enton",
        "en": "Psyduck",
        "fr": "Psykokwak"
      },
      55: {
        "de": "Entoron",
        "en": "Golduck",
        "fr": "Akwakwak"
      },
      56: {
        "de": "Menki",
        "en": "Mankey",
        "fr": "Férosinge"
      },
      57: {
        "de": "Rasaff",
        "en": "Primeape",
        "fr": "Colossinge"
      },
      58: {
        "de": "Fukano",
        "en": "Growlithe",
        "fr": "Caninos"
      },
      59: {
        "de": "Arkani",
        "en": "Arcanine",
        "fr": "Arcanin"
      },
      60: {
        "de": "Quapsel",
        "en": "Poliwag",
        "fr": "Ptitard"
      },
      61: {
        "de": "Quaputzi",
        "en": "Poliwhirl",
        "fr": "Têtarte"
      },
      62: {
        "de": "Quappo",
        "en": "Poliwrath",
        "fr": "Tartard"
      },
      63: {
        "de": "Abra",
        "en": "Abra",
        "fr": "Abra"
      },
      64: {
        "de": "Kadabra",
        "en": "Kadabra",
        "fr": "Kadabra"
      },
      65: {
        "de": "Simsala",
        "en": "Alakazam",
        "fr": "Alakazam"
      },
      66: {
        "de": "Machollo",
        "en": "Machop",
        "fr": "Machoc"
      },
      67: {
        "de": "Maschock",
        "en": "Machoke",
        "fr": "Machopeur"
      },
      68: {
        "de": "Machomei",
        "en": "Machamp",
        "fr": "Mackogneur"
      },
      69: {
        "de": "Knofensa",
        "en": "Bellsprout",
        "fr": "Chétiflor"
      },
      70: {
        "de": "Ultrigaria",
        "en": "Weepinbell",
        "fr": "Boustiflor"
      },
      71: {
        "de": "Sarzenia",
        "en": "Victreebel",
        "fr": "Empiflor"
      },
      72: {
        "de": "Tentacha",
        "en": "Tentacool",
        "fr": "Tentacool"
      },
      73: {
        "de": "Tentoxa",
        "en": "Tentacruel",
        "fr": "Tentacruel"
      },
      74: {
        "de": "Kleinstein",
        "en": "Geodude",
        "fr": "Racaillou"
      },
      75: {
        "de": "Georok",
        "en": "Graveler",
        "fr": "Gravalanch"
      },
      76: {
        "de": "Geowaz",
        "en": "Golem",
        "fr": "Grolem"
      },
      77: {
        "de": "Ponita",
        "en": "Ponyta",
        "fr": "Ponyta"
      },
      78: {
        "de": "Gallopa",
        "en": "Rapidash",
        "fr": "Galopa"
      },
      79: {
        "de": "Flegmon",
        "en": "Slowpoke",
        "fr": "Ramoloss"
      },
      80: {
        "de": "Lahmus",
        "en": "Slowbro",
        "fr": "Flagadoss"
      },
      81: {
        "de": "Magnetilo",
        "en": "Magnemite",
        "fr": "Magnéti"
      },
      82: {
        "de": "Magneton",
        "en": "Magneton",
        "fr": "Magnéton"
      },
      83: {
        "de": "Porenta",
        "en": "Farfetch'd",
        "fr": "Canarticho"
      },
      84: {
        "de": "Dodu",
        "en": "Doduo",
        "fr": "Doduo"
      },
      85: {
        "de": "Dodri",
        "en": "Dodrio",
        "fr": "Dodrio"
      },
      86: {
        "de": "Jurob",
        "en": "Seel",
        "fr": "Otaria"
      },
      87: {
        "de": "Jugong",
        "en": "Dewgong",
        "fr": "Lamantine"
      },
      88: {
        "de": "Sleima",
        "en": "Grimer",
        "fr": "Tadmorv"
      },
      89: {
        "de": "Sleimok",
        "en": "Muk",
        "fr": "Grotadmorv"
      },
      90: {
        "de": "Muschas",
        "en": "Shellder",
        "fr": "Kokiyas"
      },
      91: {
        "de": "Austos",
        "en": "Cloyster",
        "fr": "Crustabri"
      },
      92: {
        "de": "Nebulak",
        "en": "Gastly",
        "fr": "Fantominus"
      },
      93: {
        "de": "Alpollo",
        "en": "Haunter",
        "fr": "Spectrum"
      },
      94: {
        "de": "Gengar",
        "en": "Gengar",
        "fr": "Ectoplasma"
      },
      95: {
        "de": "Onix",
        "en": "Onix",
        "fr": "Onix"
      },
      96: {
        "de": "Traumato",
        "en": "Drowzee",
        "fr": "Soporifik"
      },
      97: {
        "de": "Hypno",
        "en": "Hypno",
        "fr": "Hypnomade"
      },
      98: {
        "de": "Krabby",
        "en": "Krabby",
        "fr": "Krabby"
      },
      99: {
        "de": "Kingler",
        "en": "Kingler",
        "fr": "Krabboss"
      },
      100: {
        "de": "Voltobal",
        "en": "Voltorb",
        "fr": "Voltorbe"
      },
      101: {
        "de": "Lektrobal",
        "en": "Electrode",
        "fr": "Électrode"
      },
      102: {
        "de": "Owei",
        "en": "Exeggcute",
        "fr": "Noeunoeuf"
      },
      103: {
        "de": "Kokowei",
        "en": "Exeggutor",
        "fr": "Noadkoko"
      },
      104: {
        "de": "Tragosso",
        "en": "Cubone",
        "fr": "Osselait"
      },
      105: {
        "de": "Knogga",
        "en": "Marowak",
        "fr": "Ossatueur"
      },
      106: {
        "de": "Kicklee",
        "en": "Hitmonlee",
        "fr": "Kicklee"
      },
      107: {
        "de": "Nockchan",
        "en": "Hitmonchan",
        "fr": "Tygnon"
      },
      108: {
        "de": "Schlurp",
        "en": "Lickitung",
        "fr": "Excelangue"
      },
      109: {
        "de": "Smogon",
        "en": "Koffing",
        "fr": "Smogo"
      },
      110: {
        "de": "Smogmog",
        "en": "Weezing",
        "fr": "Smogogo"
      },
      111: {
        "de": "Rihorn",
        "en": "Rhyhorn",
        "fr": "Rhinocorne"
      },
      112: {
        "de": "Rizeros",
        "en": "Rhydon",
        "fr": "Rhinoféros"
      },
      113: {
        "de": "Chaneira",
        "en": "Chansey",
        "fr": "Leveinard"
      },
      114: {
        "de": "Tangela",
        "en": "Tangela",
        "fr": "Saquedeneu"
      },
      115: {
        "de": "Kangama",
        "en": "Kangaskhan",
        "fr": "Kangourex"
      },
      116: {
        "de": "Seeper",
        "en": "Horsea",
        "fr": "Hypotrempe"
      },
      117: {
        "de": "Seemon",
        "en": "Seadra",
        "fr": "Hypocéan"
      },
      118: {
        "de": "Goldini",
        "en": "Goldeen",
        "fr": "Poissirène"
      },
      119: {
        "de": "Golking",
        "en": "Seaking",
        "fr": "Poissoroy"
      },
      120: {
        "de": "Sterndu",
        "en": "Staryu",
        "fr": "Stari"
      },
      121: {
        "de": "Starmie",
        "en": "Starmie",
        "fr": "Staross"
      },
      122: {
        "de": "Pantimos",
        "en": "Mr. Mime",
        "fr": "M. Mime"
      },
      123: {
        "de": "Sichlor",
        "en": "Scyther",
        "fr": "Insécateur"
      },
      124: {
        "de": "Rossana",
        "en": "Jynx",
        "fr": "Lippoutou"
      },
      125: {
        "de": "Elektek",
        "en": "Electabuzz",
        "fr": "Élektek"
      },
      126: {
        "de": "Magmar",
        "en": "Magmar",
        "fr": "Magmar"
      },
      127: {
        "de": "Pinsir",
        "en": "Pinsir",
        "fr": "Scarabrute"
      },
      128: {
        "de": "Tauros",
        "en": "Tauros",
        "fr": "Tauros"
      },
      129: {
        "de": "Karpador",
        "en": "Magikarp",
        "fr": "Magicarpe"
      },
      130: {
        "de": "Garados",
        "en": "Gyarados",
        "fr": "Léviator"
      },
      131: {
        "de": "Lapras",
        "en": "Lapras",
        "fr": "Lokhlass"
      },
      132: {
        "de": "Ditto",
        "en": "Ditto",
        "fr": "Métamorph"
      },
      133: {
        "de": "Evoli",
        "en": "Eevee",
        "fr": "Évoli"
      },
      134: {
        "de": "Aquana",
        "en": "Vaporeon",
        "fr": "Aquali"
      },
      135: {
        "de": "Blitza",
        "en": "Jolteon",
        "fr": "Voltali"
      },
      136: {
        "de": "Flamara",
        "en": "Flareon",
        "fr": "Pyroli"
      },
      137: {
        "de": "Porygon",
        "en": "Porygon",
        "fr": "Porygon"
      },
      138: {
        "de": "Amonitas",
        "en": "Omanyte",
        "fr": "Amonita"
      },
      139: {
        "de": "Amoroso",
        "en": "Omastar",
        "fr": "Amonistar"
      },
      140: {
        "de": "Kabuto",
        "en": "Kabuto",
        "fr": "Kabuto"
      },
      141: {
        "de": "Kabutops",
        "en": "Kabutops",
        "fr": "Kabutops"
      },
      142: {
        "de": "Aerodactyl",
        "en": "Aerodactyl",
        "fr": "Ptéra"
      },
      143: {
        "de": "Relaxo",
        "en": "Snorlax",
        "fr": "Ronflex"
      },
      144: {
        "de": "Arktos",
        "en": "Articuno",
        "fr": "Artikodin"
      },
      145: {
        "de": "Zapdos",
        "en": "Zapdos",
        "fr": "Électhor"
      },
      146: {
        "de": "Lavados",
        "en": "Moltres",
        "fr": "Sulfura"
      },
      147: {
        "de": "Dratini",
        "en": "Dratini",
        "fr": "Minidraco"
      },
      148: {
        "de": "Dragonir",
        "en": "Dragonair",
        "fr": "Draco"
      },
      149: {
        "de": "Dragoran",
        "en": "Dragonite",
        "fr": "Dracolosse"
      },
      150: {
        "de": "Mewtu",
        "en": "Mewtwo",
        "fr": "Mewtwo"
      },
      151: {
        "de": "Mew",
        "en": "Mew",
        "fr": "Mew"
      },
      152: {
        "de": "Endivie",
        "en": "Chikorita",
        "fr": "Germignon"
      },
      153: {
        "de": "Lorblatt",
        "en": "Bayleef",
        "fr": "Macronium"
      },
      154: {
        "de": "Meganie",
        "en": "Meganium",
        "fr": "Méganium"
      },
      155: {
        "de": "Feurigel",
        "en": "Cyndaquil",
        "fr": "Héricendre"
      },
      156: {
        "de": "Igelavar",
        "en": "Quilava",
        "fr": "Feurisson"
      },
      157: {
        "de": "Tornupto",
        "en": "Typhlosion",
        "fr": "Typhlosion"
      },
      158: {
        "de": "Karnimani",
        "en": "Totodile",
        "fr": "Kaiminus"
      },
      159: {
        "de": "Tyracroc",
        "en": "Croconaw",
        "fr": "Crocrodil"
      },
      160: {
        "de": "Impergator",
        "en": "Feraligatr",
        "fr": "Aligatueur"
      },
      161: {
        "de": "Wiesor",
        "en": "Sentret",
        "fr": "Fouinette"
      },
      162: {
        "de": "Wiesenior",
        "en": "Furret",
        "fr": "Fouinar"
      },
      163: {
        "de": "Hoothoot",
        "en": "Hoothoot",
        "fr": "Hoothoot"
      },
      164: {
        "de": "Noctuh",
        "en": "Noctowl",
        "fr": "Noarfang"
      },
      165: {
        "de": "Ledyba",
        "en": "Ledyba",
        "fr": "Coxy"
      },
      166: {
        "de": "Ledian",
        "en": "Ledian",
        "fr": "Coxyclaque"
      },
      167: {
        "de": "Webarak",
        "en": "Spinarak",
        "fr": "Mimigal"
      },
      168: {
        "de": "Ariados",
        "en": "Ariados",
        "fr": "Migalos"
      },
      169: {
        "de": "Iksbat",
        "en": "Crobat",
        "fr": "Nostenfer"
      },
      170: {
        "de": "Lampi",
        "en": "Chinchou",
        "fr": "Loupio"
      },
      171: {
        "de": "Lanturn",
        "en": "Lanturn",
        "fr": "Lanturn"
      },
      172: {
        "de": "Pichu",
        "en": "Pichu",
        "fr": "Pichu"
      },
      173: {
        "de": "Pii",
        "en": "Cleffa",
        "fr": "Mélo"
      },
      174: {
        "de": "Fluffeluff",
        "en": "Igglybuff",
        "fr": "Toudoudou"
      },
      175: {
        "de": "Togepi",
        "en": "Togepi",
        "fr": "Togepi"
      },
      176: {
        "de": "Togetic",
        "en": "Togetic",
        "fr": "Togetic"
      },
      177: {
        "de": "Natu",
        "en": "Natu",
        "fr": "Natu"
      },
      178: {
        "de": "Xatu",
        "en": "Xatu",
        "fr": "Xatu"
      },
      179: {
        "de": "Voltilamm",
        "en": "Mareep",
        "fr": "Wattouat"
      },
      180: {
        "de": "Waaty",
        "en": "Flaaffy",
        "fr": "Lainergie"
      },
      181: {
        "de": "Ampharos",
        "en": "Ampharos",
        "fr": "Pharamp"
      },
      182: {
        "de": "Blubella",
        "en": "Bellossom",
        "fr": "Joliflor"
      },
      183: {
        "de": "Marill",
        "en": "Marill",
        "fr": "Marill"
      },
      184: {
        "de": "Azumarill",
        "en": "Azumarill",
        "fr": "Azumarill"
      },
      185: {
        "de": "Mogelbaum",
        "en": "Sudowoodo",
        "fr": "Simularbre"
      },
      186: {
        "de": "Quaxo",
        "en": "Politoed",
        "fr": "Tarpaud"
      },
      187: {
        "de": "Hoppspross",
        "en": "Hoppip",
        "fr": "Granivol"
      },
      188: {
        "de": "Hubelupf",
        "en": "Skiploom",
        "fr": "Floravol"
      },
      189: {
        "de": "Papungha",
        "en": "Jumpluff",
        "fr": "Cotovol"
      },
      190: {
        "de": "Griffel",
        "en": "Aipom",
        "fr": "Capumain"
      },
      191: {
        "de": "Sonnkern",
        "en": "Sunkern",
        "fr": "Tournegrin"
      },
      192: {
        "de": "Sonnflora",
        "en": "Sunflora",
        "fr": "Héliatronc"
      },
      193: {
        "de": "Yanma",
        "en": "Yanma",
        "fr": "Yanma"
      },
      194: {
        "de": "Felino",
        "en": "Wooper",
        "fr": "Axoloto"
      },
      195: {
        "de": "Morlord",
        "en": "Quagsire",
        "fr": "Maraiste"
      },
      196: {
        "de": "Psiana",
        "en": "Espeon",
        "fr": "Mentali"
      },
      197: {
        "de": "Nachtara",
        "en": "Umbreon",
        "fr": "Noctali"
      },
      198: {
        "de": "Kramurx",
        "en": "Murkrow",
        "fr": "Cornèbre"
      },
      199: {
        "de": "Laschoking",
        "en": "Slowking",
        "fr": "Roigada"
      },
      200: {
        "de": "Traunfugil",
        "en": "Misdreavus",
        "fr": "Feuforêve"
      },
      201: {
        "de": "Icognito",
        "en": "Unown",
        "fr": "Zarbi"
      },
      202: {
        "de": "Woingenau",
        "en": "Wobbuffet",
        "fr": "Qulbutoké"
      },
      203: {
        "de": "Girafarig",
        "en": "Girafarig",
        "fr": "Girafarig"
      },
      204: {
        "de": "Tannza",
        "en": "Pineco",
        "fr": "Pomdepik"
      },
      205: {
        "de": "Forstellka",
        "en": "Forretress",
        "fr": "Foretress"
      },
      206: {
        "de": "Dummisel",
        "en": "Dunsparce",
        "fr": "Insolourdo"
      },
      207: {
        "de": "Skorgla",
        "en": "Gligar",
        "fr": "Scorplane"
      },
      208: {
        "de": "Stahlos",
        "en": "Steelix",
        "fr": "Steelix"
      },
      209: {
        "de": "Snubbull",
        "en": "Snubbull",
        "fr": "Snubbull"
      },
      210: {
        "de": "Granbull",
        "en": "Granbull",
        "fr": "Granbull"
      },
      211: {
        "de": "Baldorfish",
        "en": "Qwilfish",
        "fr": "Qwilfish"
      },
      212: {
        "de": "Scherox",
        "en": "Scizor",
        "fr": "Cizayox"
      },
      213: {
        "de": "Pottrott",
        "en": "Shuckle",
        "fr": "Caratroc"
      },
      214: {
        "de": "Skaraborn",
        "en": "Heracross",
        "fr": "Scarhino"
      },
      215: {
        "de": "Sniebel",
        "en": "Sneasel",
        "fr": "Farfuret"
      },
      216: {
        "de": "Teddiursa",
        "en": "Teddiursa",
        "fr": "Teddiursa"
      },
      217: {
        "de": "Ursaring",
        "en": "Ursaring",
        "fr": "Ursaring"
      },
      218: {
        "de": "Schneckmag",
        "en": "Slugma",
        "fr": "Limagma"
      },
      219: {
        "de": "Magcargo",
        "en": "Magcargo",
        "fr": "Volcaropod"
      },
      220: {
        "de": "Quiekel",
        "en": "Swinub",
        "fr": "Marcacrin"
      },
      221: {
        "de": "Keifel",
        "en": "Piloswine",
        "fr": "Cochignon"
      },
      222: {
        "de": "Corasonn",
        "en": "Corsola",
        "fr": "Corayon"
      },
      223: {
        "de": "Remoraid",
        "en": "Remoraid",
        "fr": "Rémoraid"
      },
      224: {
        "de": "Octillery",
        "en": "Octillery",
        "fr": "Octillery"
      },
      225: {
        "de": "Botogel",
        "en": "Delibird",
        "fr": "Cadoizo"
      },
      226: {
        "de": "Mantax",
        "en": "Mantine",
        "fr": "Démanta"
      },
      227: {
        "de": "Panzaeron",
        "en": "Skarmory",
        "fr": "Airmure"
      },
      228: {
        "de": "Hunduster",
        "en": "Houndour",
        "fr": "Malosse"
      },
      229: {
        "de": "Hundemon",
        "en": "Houndoom",
        "fr": "Démolosse"
      },
      230: {
        "de": "Seedraking",
        "en": "Kingdra",
        "fr": "Hyporoi"
      },
      231: {
        "de": "Phanpy",
        "en": "Phanpy",
        "fr": "Phanpy"
      },
      232: {
        "de": "Donphan",
        "en": "Donphan",
        "fr": "Donphan"
      },
      233: {
        "de": "Porygon2",
        "en": "Porygon2",
        "fr": "Porygon2"
      },
      234: {
        "de": "Damhirplex",
        "en": "Stantler",
        "fr": "Cerfrousse"
      },
      235: {
        "de": "Farbeagle",
        "en": "Smeargle",
        "fr": "Queulorior"
      },
      236: {
        "de": "Rabauz",
        "en": "Tyrogue",
        "fr": "Debugant"
      },
      237: {
        "de": "Kapoera",
        "en": "Hitmontop",
        "fr": "Kapoera"
      },
      238: {
        "de": "Kussilla",
        "en": "Smoochum",
        "fr": "Lippouti"
      },
      239: {
        "de": "Elekid",
        "en": "Elekid",
        "fr": "Élekid"
      },
      240: {
        "de": "Magby",
        "en": "Magby",
        "fr": "Magby"
      },
      241: {
        "de": "Miltank",
        "en": "Miltank",
        "fr": "Écrémeuh"
      },
      242: {
        "de": "Heiteira",
        "en": "Blissey",
        "fr": "Leuphorie"
      },
      243: {
        "de": "Raikou",
        "en": "Raikou",
        "fr": "Raikou"
      },
      244: {
        "de": "Entei",
        "en": "Entei",
        "fr": "Entei"
      },
      245: {
        "de": "Suicune",
        "en": "Suicune",
        "fr": "Suicune"
      },
      246: {
        "de": "Larvitar",
        "en": "Larvitar",
        "fr": "Embrylex"
      },
      247: {
        "de": "Pupitar",
        "en": "Pupitar",
        "fr": "Ymphect"
      },
      248: {
        "de": "Despotar",
        "en": "Tyranitar",
        "fr": "Tyranocif"
      },
      249: {
        "de": "Lugia",
        "en": "Lugia",
        "fr": "Lugia"
      },
      250: {
        "de": "Ho-Oh",
        "en": "Ho-Oh",
        "fr": "Ho-Oh"
      },
      251: {
        "de": "Celebi",
        "en": "Celebi",
        "fr": "Celebi"
      },
      252: {
        "de": "Geckarbor",
        "en": "Treecko",
        "fr": "Arcko"
      },
      253: {
        "de": "Reptain",
        "en": "Grovyle",
        "fr": "Massko"
      },
      254: {
        "de": "Gewaldro",
        "en": "Sceptile",
        "fr": "Jungko"
      },
      255: {
        "de": "Flemmli",
        "en": "Torchic",
        "fr": "Poussifeu"
      },
      256: {
        "de": "Jungglut",
        "en": "Combusken",
        "fr": "Galifeu"
      },
      257: {
        "de": "Lohgock",
        "en": "Blaziken",
        "fr": "Braségali"
      },
      258: {
        "de": "Hydropi",
        "en": "Mudkip",
        "fr": "Gobou"
      },
      259: {
        "de": "Moorabbel",
        "en": "Marshtomp",
        "fr": "Flobio"
      },
      260: {
        "de": "Sumpex",
        "en": "Swampert",
        "fr": "Laggron"
      },
      261: {
        "de": "Fiffyen",
        "en": "Poochyena",
        "fr": "Medhyèna"
      },
      262: {
        "de": "Magnayen",
        "en": "Mightyena",
        "fr": "Grahyèna"
      },
      263: {
        "de": "Zigzachs",
        "en": "Zigzagoon",
        "fr": "Zigzaton"
      },
      264: {
        "de": "Geradaks",
        "en": "Linoone",
        "fr": "Linéon"
      },
      265: {
        "de": "Waumpel",
        "en": "Wurmple",
        "fr": "Chenipotte"
      },
      266: {
        "de": "Schaloko",
        "en": "Silcoon",
        "fr": "Armulys"
      },
      267: {
        "de": "Papinella",
        "en": "Beautifly",
        "fr": "Charmillon"
      },
      268: {
        "de": "Panekon",
        "en": "Cascoon",
        "fr": "Blindalys"
      },
      269: {
        "de": "Pudox",
        "en": "Dustox",
        "fr": "Papinox"
      },
      270: {
        "de": "Loturzel",
        "en": "Lotad",
        "fr": "Nénupiot"
      },
      271: {
        "de": "Lombrero",
        "en": "Lombre",
        "fr": "Lombre"
      },
      272: {
        "de": "Kappalores",
        "en": "Ludicolo",
        "fr": "Ludicolo"
      },
      273: {
        "de": "Samurzel",
        "en": "Seedot",
        "fr": "Grainipiot"
      },
      274: {
        "de": "Blanas",
        "en": "Nuzleaf",
        "fr": "Pifeuil"
      },
      275: {
        "de": "Tengulist",
        "en": "Shiftry",
        "fr": "Tengalice"
      },
      276: {
        "de": "Schwalbini",
        "en": "Taillow",
        "fr": "Nirondelle"
      },
      277: {
        "de": "Schwalboss",
        "en": "Swellow",
        "fr": "Hélédelle"
      },
      278: {
        "de": "Wingull",
        "en": "Wingull",
        "fr": "Goélise"
      },
      279: {
        "de": "Pelipper",
        "en": "Pelipper",
        "fr": "Bekipan"
      },
      280: {
        "de": "Trasla",
        "en": "Ralts",
        "fr": "Tarsal"
      },
      281: {
        "de": "Kirlia",
        "en": "Kirlia",
        "fr": "Kirlia"
      },
      282: {
        "de": "Guardevoir",
        "en": "Gardevoir",
        "fr": "Gardevoir"
      },
      283: {
        "de": "Gehweiher",
        "en": "Surskit",
        "fr": "Arakdo"
      },
      284: {
        "de": "Maskeregen",
        "en": "Masquerain",
        "fr": "Maskadra"
      },
      285: {
        "de": "Knilz",
        "en": "Shroomish",
        "fr": "Balignon"
      },
      286: {
        "de": "Kapilz",
        "en": "Breloom",
        "fr": "Chapignon"
      },
      287: {
        "de": "Bummelz",
        "en": "Slakoth",
        "fr": "Parecool"
      },
      288: {
        "de": "Muntier",
        "en": "Vigoroth",
        "fr": "Vigoroth"
      },
      289: {
        "de": "Letarking",
        "en": "Slaking",
        "fr": "Monaflèmit"
      },
      290: {
        "de": "Nincada",
        "en": "Nincada",
        "fr": "Ningale"
      },
      291: {
        "de": "Ninjask",
        "en": "Ninjask",
        "fr": "Ninjask"
      },
      292: {
        "de": "Ninjatom",
        "en": "Shedinja",
        "fr": "Munja"
      },
      293: {
        "de": "Flurmel",
        "en": "Whismur",
        "fr": "Chuchmur"
      },
      294: {
        "de": "Krakeelo",
        "en": "Loudred",
        "fr": "Ramboum"
      },
      295: {
        "de": "Krawumms",
        "en": "Exploud",
        "fr": "Brouhabam"
      },
      296: {
        "de": "Makuhita",
        "en": "Makuhita",
        "fr": "Makuhita"
      },
      297: {
        "de": "Hariyama",
        "en": "Hariyama",
        "fr": "Hariyama"
      },
      298: {
        "de": "Azurill",
        "en": "Azurill",
        "fr": "Azurill"
      },
      299: {
        "de": "Nasgnet",
        "en": "Nosepass",
        "fr": "Tarinor"
      },
      300: {
        "de": "Eneco",
        "en": "Skitty",
        "fr": "Skitty"
      },
      301: {
        "de": "Enekoro",
        "en": "Delcatty",
        "fr": "Delcatty"
      },
      302: {
        "de": "Zobiris",
        "en": "Sableye",
        "fr": "Ténéfix"
      },
      303: {
        "de": "Flunkifer",
        "en": "Mawile",
        "fr": "Mysdibule"
      },
      304: {
        "de": "Stollunior",
        "en": "Aron",
        "fr": "Galekid"
      },
      305: {
        "de": "Stollrak",
        "en": "Lairon",
        "fr": "Galegon"
      },
      306: {
        "de": "Stolloss",
        "en": "Aggron",
        "fr": "Galeking"
      },
      307: {
        "de": "Meditie",
        "en": "Meditite",
        "fr": "Méditikka"
      },
      308: {
        "de": "Meditalis",
        "en": "Medicham",
        "fr": "Charmina"
      },
      309: {
        "de": "Frizelbliz",
        "en": "Electrike",
        "fr": "Dynavolt"
      },
      310: {
        "de": "Voltenso",
        "en": "Manectric",
        "fr": "Élecsprint"
      },
      311: {
        "de": "Plusle",
        "en": "Plusle",
        "fr": "Posipi"
      },
      312: {
        "de": "Minun",
        "en": "Minun",
        "fr": "Négapi"
      },
      313: {
        "de": "Volbeat",
        "en": "Volbeat",
        "fr": "Muciole"
      },
      314: {
        "de": "Illumise",
        "en": "Illumise",
        "fr": "Lumivole"
      },
      315: {
        "de": "Roselia",
        "en": "Roselia",
        "fr": "Rosélia"
      },
      316: {
        "de": "Schluppuck",
        "en": "Gulpin",
        "fr": "Gloupti"
      },
      317: {
        "de": "Schlukwech",
        "en": "Swalot",
        "fr": "Avaltout"
      },
      318: {
        "de": "Kanivanha",
        "en": "Carvanha",
        "fr": "Carvanha"
      },
      319: {
        "de": "Tohaido",
        "en": "Sharpedo",
        "fr": "Sharpedo"
      },
      320: {
        "de": "Wailmer",
        "en": "Wailmer",
        "fr": "Wailmer"
      },
      321: {
        "de": "Wailord",
        "en": "Wailord",
        "fr": "Wailord"
      },
      322: {
        "de": "Camaub",
        "en": "Numel",
        "fr": "Chamallot"
      },
      323: {
        "de": "Camerupt",
        "en": "Camerupt",
        "fr": "Camérupt"
      },
      324: {
        "de": "Qurtel",
        "en": "Torkoal",
        "fr": "Chartor"
      },
      325: {
        "de": "Spoink",
        "en": "Spoink",
        "fr": "Spoink"
      },
      326: {
        "de": "Groink",
        "en": "Grumpig",
        "fr": "Groret"
      },
      327: {
        "de": "Pandir",
        "en": "Spinda",
        "fr": "Spinda"
      },
      328: {
        "de": "Knacklion",
        "en": "Trapinch",
        "fr": "Kraknoix"
      },
      329: {
        "de": "Vibrava",
        "en": "Vibrava",
        "fr": "Vibraninf"
      },
      330: {
        "de": "Libelldra",
        "en": "Flygon",
        "fr": "Libégon"
      },
      331: {
        "de": "Tuska",
        "en": "Cacnea",
        "fr": "Cacnea"
      },
      332: {
        "de": "Noktuska",
        "en": "Cacturne",
        "fr": "Cacturne"
      },
      333: {
        "de": "Wablu",
        "en": "Swablu",
        "fr": "Tylton"
      },
      334: {
        "de": "Altaria",
        "en": "Altaria",
        "fr": "Altaria"
      },
      335: {
        "de": "Sengo",
        "en": "Zangoose",
        "fr": "Mangriff"
      },
      336: {
        "de": "Vipitis",
        "en": "Seviper",
        "fr": "Séviper"
      },
      337: {
        "de": "Lunastein",
        "en": "Lunatone",
        "fr": "Séléroc"
      },
      338: {
        "de": "Sonnfel",
        "en": "Solrock",
        "fr": "Solaroc"
      },
      339: {
        "de": "Schmerbe",
        "en": "Barboach",
        "fr": "Barloche"
      },
      340: {
        "de": "Welsar",
        "en": "Whiscash",
        "fr": "Barbicha"
      },
      341: {
        "de": "Krebscorps",
        "en": "Corphish",
        "fr": "Écrapince"
      },
      342: {
        "de": "Krebutack",
        "en": "Crawdaunt",
        "fr": "Colhomard"
      },
      343: {
        "de": "Puppance",
        "en": "Baltoy",
        "fr": "Balbuto"
      },
      344: {
        "de": "Lepumentas",
        "en": "Claydol",
        "fr": "Kaorine"
      },
      345: {
        "de": "Liliep",
        "en": "Lileep",
        "fr": "Lilia"
      },
      346: {
        "de": "Wielie",
        "en": "Cradily",
        "fr": "Vacilys"
      },
      347: {
        "de": "Anorith",
        "en": "Anorith",
        "fr": "Anorith"
      },
      348: {
        "de": "Armaldo",
        "en": "Armaldo",
        "fr": "Armaldo"
      },
      349: {
        "de": "Barschwa",
        "en": "Feebas",
        "fr": "Barpau"
      },
      350: {
        "de": "Milotic",
        "en": "Milotic",
        "fr": "Milobellus"
      },
      351: {
        "de": "Formeo",
        "en": "Castform",
        "fr": "Morphéo"
      },
      352: {
        "de": "Kecleon",
        "en": "Kecleon",
        "fr": "Kecleon"
      },
      353: {
        "de": "Shuppet",
        "en": "Shuppet",
        "fr": "Polichombr"
      },
      354: {
        "de": "Banette",
        "en": "Banette",
        "fr": "Branette"
      },
      355: {
        "de": "Zwirrlicht",
        "en": "Duskull",
        "fr": "Skelénox"
      },
      356: {
        "de": "Zwirrklop",
        "en": "Dusclops",
        "fr": "Téraclope"
      },
      357: {
        "de": "Tropius",
        "en": "Tropius",
        "fr": "Tropius"
      },
      358: {
        "de": "Palimpalim",
        "en": "Chimecho",
        "fr": "Éoko"
      },
      359: {
        "de": "Absol",
        "en": "Absol",
        "fr": "Absol"
      },
      360: {
        "de": "Isso",
        "en": "Wynaut",
        "fr": "Okéoké"
      },
      361: {
        "de": "Schneppke",
        "en": "Snorunt",
        "fr": "Stalgamin"
      },
      362: {
        "de": "Firnontor",
        "en": "Glalie",
        "fr": "Oniglali"
      },
      363: {
        "de": "Seemops",
        "en": "Spheal",
        "fr": "Obalie"
      },
      364: {
        "de": "Seejong",
        "en": "Sealeo",
        "fr": "Phogleur"
      },
      365: {
        "de": "Walraisa",
        "en": "Walrein",
        "fr": "Kaimorse"
      },
      366: {
        "de": "Perlu",
        "en": "Clamperl",
        "fr": "Coquiperl"
      },
      367: {
        "de": "Aalabyss",
        "en": "Huntail",
        "fr": "Serpang"
      },
      368: {
        "de": "Saganabyss",
        "en": "Gorebyss",
        "fr": "Rosabyss"
      },
      369: {
        "de": "Relicanth",
        "en": "Relicanth",
        "fr": "Relicanth"
      },
      370: {
        "de": "Liebiskus",
        "en": "Luvdisc",
        "fr": "Lovdisc"
      },
      371: {
        "de": "Kindwurm",
        "en": "Bagon",
        "fr": "Draby"
      },
      372: {
        "de": "Draschel",
        "en": "Shelgon",
        "fr": "Drackhaus"
      },
      373: {
        "de": "Brutalanda",
        "en": "Salamence",
        "fr": "Drattak"
      },
      374: {
        "de": "Tanhel",
        "en": "Beldum",
        "fr": "Terhal"
      },
      375: {
        "de": "Metang",
        "en": "Metang",
        "fr": "Métang"
      },
      376: {
        "de": "Metagross",
        "en": "Metagross",
        "fr": "Métalosse"
      },
      377: {
        "de": "Regirock",
        "en": "Regirock",
        "fr": "Regirock"
      },
      378: {
        "de": "Regice",
        "en": "Regice",
        "fr": "Regice"
      },
      379: {
        "de": "Registeel",
        "en": "Registeel",
        "fr": "Registeel"
      },
      380: {
        "de": "Latias",
        "en": "Latias",
        "fr": "Latias"
      },
      381: {
        "de": "Latios",
        "en": "Latios",
        "fr": "Latios"
      },
      382: {
        "de": "Kyogre",
        "en": "Kyogre",
        "fr": "Kyogre"
      },
      383: {
        "de": "Groudon",
        "en": "Groudon",
        "fr": "Groudon"
      },
      384: {
        "de": "Rayquaza",
        "en": "Rayquaza",
        "fr": "Rayquaza"
      },
      385: {
        "de": "Jirachi",
        "en": "Jirachi",
        "fr": "Jirachi"
      },
      386: {
        "de": "Deoxys",
        "en": "Deoxys",
        "fr": "Deoxys"
      },
      387: {
        "de": "Chelast",
        "en": "Turtwig",
        "fr": "Tortipouss"
      },
      388: {
        "de": "Chelcarain",
        "en": "Grotle",
        "fr": "Boskara"
      },
      389: {
        "de": "Chelterrar",
        "en": "Torterra",
        "fr": "Torterra"
      },
      390: {
        "de": "Panflam",
        "en": "Chimchar",
        "fr": "Ouisticram"
      },
      391: {
        "de": "Panpyro",
        "en": "Monferno",
        "fr": "Chimpenfeu"
      },
      392: {
        "de": "Panferno",
        "en": "Infernape",
        "fr": "Simiabraz"
      },
      393: {
        "de": "Plinfa",
        "en": "Piplup",
        "fr": "Tiplouf"
      },
      394: {
        "de": "Pliprin",
        "en": "Prinplup",
        "fr": "Prinplouf"
      },
      395: {
        "de": "Impoleon",
        "en": "Empoleon",
        "fr": "Pingoléon"
      },
      396: {
        "de": "Staralili",
        "en": "Starly",
        "fr": "Étourmi"
      },
      397: {
        "de": "Staravia",
        "en": "Staravia",
        "fr": "Étourvol"
      },
      398: {
        "de": "Staraptor",
        "en": "Staraptor",
        "fr": "Étouraptor"
      },
      399: {
        "de": "Bidiza",
        "en": "Bidoof",
        "fr": "Keunotor"
      },
      400: {
        "de": "Bidifas",
        "en": "Bibarel",
        "fr": "Castorno"
      },
      401: {
        "de": "Zirpurze",
        "en": "Kricketot",
        "fr": "Crikzik"
      },
      402: {
        "de": "Zirpeise",
        "en": "Kricketune",
        "fr": "Mélokrik"
      },
      403: {
        "de": "Sheinux",
        "en": "Shinx",
        "fr": "Lixy"
      },
      404: {
        "de": "Luxio",
        "en": "Luxio",
        "fr": "Luxio"
      },
      405: {
        "de": "Luxtra",
        "en": "Luxray",
        "fr": "Luxray"
      },
      406: {
        "de": "Knospi",
        "en": "Budew",
        "fr": "Rozbouton"
      },
      407: {
        "de": "Roserade",
        "en": "Roserade",
        "fr": "Roserade"
      },
      408: {
        "de": "Koknodon",
        "en": "Cranidos",
        "fr": "Kranidos"
      },
      409: {
        "de": "Rameidon",
        "en": "Rampardos",
        "fr": "Charkos"
      },
      410: {
        "de": "Schilterus",
        "en": "Shieldon",
        "fr": "Dinoclier"
      },
      411: {
        "de": "Bollterus",
        "en": "Bastiodon",
        "fr": "Bastiodon"
      },
      412: {
        "de": "Burmy",
        "en": "Burmy",
        "fr": "Cheniti"
      },
      413: {
        "de": "Burmadame",
        "en": "Wormadam",
        "fr": "Cheniselle"
      },
      414: {
        "de": "Moterpel",
        "en": "Mothim",
        "fr": "Papilord"
      },
      415: {
        "de": "Wadribie",
        "en": "Combee",
        "fr": "Apitrini"
      },
      416: {
        "de": "Honweisel",
        "en": "Vespiquen",
        "fr": "Apireine"
      },
      417: {
        "de": "Pachirisu",
        "en": "Pachirisu",
        "fr": "Pachirisu"
      },
      418: {
        "de": "Bamelin",
        "en": "Buizel",
        "fr": "Mustébouée"
      },
      419: {
        "de": "Bojelin",
        "en": "Floatzel",
        "fr": "Mustéflott"
      },
      420: {
        "de": "Kikugi",
        "en": "Cherubi",
        "fr": "Ceribou"
      },
      421: {
        "de": "Kinoso",
        "en": "Cherrim",
        "fr": "Ceriflor"
      },
      422: {
        "de": "Schalellos",
        "en": "Shellos",
        "fr": "Sancoki"
      },
      423: {
        "de": "Gastrodon",
        "en": "Gastrodon",
        "fr": "Tritosor"
      },
      424: {
        "de": "Ambidiffel",
        "en": "Ambipom",
        "fr": "Capidextre"
      },
      425: {
        "de": "Driftlon",
        "en": "Drifloon",
        "fr": "Baudrive"
      },
      426: {
        "de": "Drifzepeli",
        "en": "Drifblim",
        "fr": "Grodrive"
      },
      427: {
        "de": "Haspiror",
        "en": "Buneary",
        "fr": "Laporeille"
      },
      428: {
        "de": "Schlapor",
        "en": "Lopunny",
        "fr": "Lockpin"
      },
      429: {
        "de": "Traunmagil",
        "en": "Mismagius",
        "fr": "Magirêve"
      },
      430: {
        "de": "Kramshef",
        "en": "Honchkrow",
        "fr": "Corboss"
      },
      431: {
        "de": "Charmian",
        "en": "Glameow",
        "fr": "Chaglam"
      },
      432: {
        "de": "Shnurgarst",
        "en": "Purugly",
        "fr": "Chaffreux"
      },
      433: {
        "de": "Klingplim",
        "en": "Chingling",
        "fr": "Korillon"
      },
      434: {
        "de": "Skunkapuh",
        "en": "Stunky",
        "fr": "Moufouette"
      },
      435: {
        "de": "Skunktank",
        "en": "Skuntank",
        "fr": "Moufflair"
      },
      436: {
        "de": "Bronzel",
        "en": "Bronzor",
        "fr": "Archéomire"
      },
      437: {
        "de": "Bronzong",
        "en": "Bronzong",
        "fr": "Archéodong"
      },
      438: {
        "de": "Mobai",
        "en": "Bonsly",
        "fr": "Manzaï"
      },
      439: {
        "de": "Pantimimi",
        "en": "Mime Jr.",
        "fr": "Mime Jr"
      },
      440: {
        "de": "Wonneira",
        "en": "Happiny",
        "fr": "Ptiravi"
      },
      441: {
        "de": "Plaudagei",
        "en": "Chatot",
        "fr": "Pijako"
      },
      442: {
        "de": "Kryppuk",
        "en": "Spiritomb",
        "fr": "Spiritomb"
      },
      443: {
        "de": "Kaumalat",
        "en": "Gible",
        "fr": "Griknot"
      },
      444: {
        "de": "Knarksel",
        "en": "Gabite",
        "fr": "Carmache"
      },
      445: {
        "de": "Knakrack",
        "en": "Garchomp",
        "fr": "Carchacrok"
      },
      446: {
        "de": "Mampfaxo",
        "en": "Munchlax",
        "fr": "Goinfrex"
      },
      447: {
        "de": "Riolu",
        "en": "Riolu",
        "fr": "Riolu"
      },
      448: {
        "de": "Lucario",
        "en": "Lucario",
        "fr": "Lucario"
      },
      449: {
        "de": "Hippopotas",
        "en": "Hippopotas",
        "fr": "Hippopotas"
      },
      450: {
        "de": "Hippoterus",
        "en": "Hippowdon",
        "fr": "Hippodocus"
      },
      451: {
        "de": "Pionskora",
        "en": "Skorupi",
        "fr": "Rapion"
      },
      452: {
        "de": "Piondragi",
        "en": "Drapion",
        "fr": "Drascore"
      },
      453: {
        "de": "Glibunkel",
        "en": "Croagunk",
        "fr": "Cradopaud"
      },
      454: {
        "de": "Toxiquak",
        "en": "Toxicroak",
        "fr": "Coatox"
      },
      455: {
        "de": "Venuflibis",
        "en": "Carnivine",
        "fr": "Vortente"
      },
      456: {
        "de": "Finneon",
        "en": "Finneon",
        "fr": "Écayon"
      },
      457: {
        "de": "Lumineon",
        "en": "Lumineon",
        "fr": "Luminéon"
      },
      458: {
        "de": "Mantirps",
        "en": "Mantyke",
        "fr": "Babimanta"
      },
      459: {
        "de": "Shnebedeck",
        "en": "Snover",
        "fr": "Blizzi"
      },
      460: {
        "de": "Rexblisar",
        "en": "Abomasnow",
        "fr": "Blizzaroi"
      },
      461: {
        "de": "Snibunna",
        "en": "Weavile",
        "fr": "Dimoret"
      },
      462: {
        "de": "Magnezone",
        "en": "Magnezone",
        "fr": "Magnézone"
      },
      463: {
        "de": "Schlurplek",
        "en": "Lickilicky",
        "fr": "Coudlangue"
      },
      464: {
        "de": "Rihornior",
        "en": "Rhyperior",
        "fr": "Rhinastoc"
      },
      465: {
        "de": "Tangoloss",
        "en": "Tangrowth",
        "fr": "Bouldeneu"
      },
      466: {
        "de": "Elevoltek",
        "en": "Electivire",
        "fr": "Élekable"
      },
      467: {
        "de": "Magbrant",
        "en": "Magmortar",
        "fr": "Maganon"
      },
      468: {
        "de": "Togekiss",
        "en": "Togekiss",
        "fr": "Togekiss"
      },
      469: {
        "de": "Yanmega",
        "en": "Yanmega",
        "fr": "Yanmega"
      },
      470: {
        "de": "Folipurba",
        "en": "Leafeon",
        "fr": "Phyllali"
      },
      471: {
        "de": "Glaziola",
        "en": "Glaceon",
        "fr": "Givrali"
      },
      472: {
        "de": "Skorgro",
        "en": "Gliscor",
        "fr": "Scorvol"
      },
      473: {
        "de": "Mamutel",
        "en": "Mamoswine",
        "fr": "Mammochon"
      },
      474: {
        "de": "Porygon-Z",
        "en": "Porygon-Z",
        "fr": "Porygon-Z"
      },
      475: {
        "de": "Galagladi",
        "en": "Gallade",
        "fr": "Gallame"
      },
      476: {
        "de": "Voluminas",
        "en": "Probopass",
        "fr": "Tarinorme"
      },
      477: {
        "de": "Zwirrfinst",
        "en": "Dusknoir",
        "fr": "Noctunoir"
      },
      478: {
        "de": "Frosdedje",
        "en": "Froslass",
        "fr": "Momartik"
      },
      479: {
        "de": "Rotom",
        "en": "Rotom",
        "fr": "Motisma"
      },
      480: {
        "de": "Selfe",
        "en": "Uxie",
        "fr": "Créhelf"
      },
      481: {
        "de": "Vesprit",
        "en": "Mesprit",
        "fr": "Créfollet"
      },
      482: {
        "de": "Tobutz",
        "en": "Azelf",
        "fr": "Créfadet"
      },
      483: {
        "de": "Dialga",
        "en": "Dialga",
        "fr": "Dialga"
      },
      484: {
        "de": "Palkia",
        "en": "Palkia",
        "fr": "Palkia"
      },
      485: {
        "de": "Heatran",
        "en": "Heatran",
        "fr": "Heatran"
      },
      486: {
        "de": "Regigigas",
        "en": "Regigigas",
        "fr": "Regigigas"
      },
      487: {
        "de": "Giratina",
        "en": "Giratina",
        "fr": "Giratina"
      },
      488: {
        "de": "Cresselia",
        "en": "Cresselia",
        "fr": "Cresselia"
      },
      489: {
        "de": "Phione",
        "en": "Phione",
        "fr": "Phione"
      },
      490: {
        "de": "Manaphy",
        "en": "Manaphy",
        "fr": "Manaphy"
      },
      491: {
        "de": "Darkrai",
        "en": "Darkrai",
        "fr": "Darkrai"
      },
      492: {
        "de": "Shaymin",
        "en": "Shaymin",
        "fr": "Shaymin"
      },
      493: {
        "de": "Arceus",
        "en": "Arceus",
        "fr": "Arceus"
      },
      494: {
        "de": "Victini",
        "en": "Victini",
        "fr": "Victini"
      },
      495: {
        "de": "Serpifeu",
        "en": "Snivy",
        "fr": "Vipélierre"
      },
      496: {
        "de": "Efoserp",
        "en": "Servine",
        "fr": "Lianaja"
      },
      497: {
        "de": "Serpiroyal",
        "en": "Serperior",
        "fr": "Majaspic"
      },
      498: {
        "de": "Floink",
        "en": "Tepig",
        "fr": "Gruikui"
      },
      499: {
        "de": "Ferkokel",
        "en": "Pignite",
        "fr": "Grotichon"
      },
      500: {
        "de": "Flambirex",
        "en": "Emboar",
        "fr": "Roitiflam"
      },
      501: {
        "de": "Ottaro",
        "en": "Oshawott",
        "fr": "Moustillon"
      },
      502: {
        "de": "Zwottronin",
        "en": "Dewott",
        "fr": "Mateloutre"
      },
      503: {
        "de": "Admurai",
        "en": "Samurott",
        "fr": "Clamiral"
      },
      504: {
        "de": "Nagelotz",
        "en": "Patrat",
        "fr": "Ratentif"
      },
      505: {
        "de": "Kukmarda",
        "en": "Watchog",
        "fr": "Miradar"
      },
      506: {
        "de": "Yorkleff",
        "en": "Lillipup",
        "fr": "Ponchiot"
      },
      507: {
        "de": "Terribark",
        "en": "Herdier",
        "fr": "Ponchien"
      },
      508: {
        "de": "Bissbark",
        "en": "Stoutland",
        "fr": "Mastouffe"
      },
      509: {
        "de": "Felilou",
        "en": "Purrloin",
        "fr": "Chacripan"
      },
      510: {
        "de": "Kleoparda",
        "en": "Liepard",
        "fr": "Léopardus"
      },
      511: {
        "de": "Vegimak",
        "en": "Pansage",
        "fr": "Feuillajou"
      },
      512: {
        "de": "Vegichita",
        "en": "Simisage",
        "fr": "Feuiloutan"
      },
      513: {
        "de": "Grillmak",
        "en": "Pansear",
        "fr": "Flamajou"
      },
      514: {
        "de": "Grillchita",
        "en": "Simisear",
        "fr": "Flamoutan"
      },
      515: {
        "de": "Sodamak",
        "en": "Panpour",
        "fr": "Flotajou"
      },
      516: {
        "de": "Sodachita",
        "en": "Simipour",
        "fr": "Flotoutan"
      },
      517: {
        "de": "Somniam",
        "en": "Munna",
        "fr": "Munna"
      },
      518: {
        "de": "Somnivora",
        "en": "Musharna",
        "fr": "Mushana"
      },
      519: {
        "de": "Dusselgurr",
        "en": "Pidove",
        "fr": "Poichigeon"
      },
      520: {
        "de": "Navitaub",
        "en": "Tranquill",
        "fr": "Colombeau"
      },
      521: {
        "de": "Fasasnob",
        "en": "Unfezant",
        "fr": "Déflaisan"
      },
      522: {
        "de": "Elezeba",
        "en": "Blitzle",
        "fr": "Zébibron"
      },
      523: {
        "de": "Zebritz",
        "en": "Zebstrika",
        "fr": "Zéblitz"
      },
      524: {
        "de": "Kiesling",
        "en": "Roggenrola",
        "fr": "Nodulithe"
      },
      525: {
        "de": "Sedimantur",
        "en": "Boldore",
        "fr": "Géolithe"
      },
      526: {
        "de": "Brockoloss",
        "en": "Gigalith",
        "fr": "Gigalithe"
      },
      527: {
        "de": "Fleknoil",
        "en": "Woobat",
        "fr": "Chovsourir"
      },
      528: {
        "de": "Fletiamo",
        "en": "Swoobat",
        "fr": "Rhinolove"
      },
      529: {
        "de": "Rotomurf",
        "en": "Drilbur",
        "fr": "Rototaupe"
      },
      530: {
        "de": "Stalobor",
        "en": "Excadrill",
        "fr": "Minotaupe"
      },
      531: {
        "de": "Ohrdoch",
        "en": "Audino",
        "fr": "Nanméouïe"
      },
      532: {
        "de": "Praktibalk",
        "en": "Timburr",
        "fr": "Charpenti"
      },
      533: {
        "de": "Strepoli",
        "en": "Gurdurr",
        "fr": "Ouvrifier"
      },
      534: {
        "de": "Meistagrif",
        "en": "Conkeldurr",
        "fr": "Bétochef"
      },
      535: {
        "de": "Schallquap",
        "en": "Tympole",
        "fr": "Tritonde"
      },
      536: {
        "de": "Mebrana",
        "en": "Palpitoad",
        "fr": "Batracné"
      },
      537: {
        "de": "Branawarz",
        "en": "Seismitoad",
        "fr": "Crapustule"
      },
      538: {
        "de": "Jiutesto",
        "en": "Throh",
        "fr": "Judokrak"
      },
      539: {
        "de": "Karadonis",
        "en": "Sawk",
        "fr": "Karaclée"
      },
      540: {
        "de": "Strawickl",
        "en": "Sewaddle",
        "fr": "Larveyette"
      },
      541: {
        "de": "Folikon",
        "en": "Swadloon",
        "fr": "Couverdure"
      },
      542: {
        "de": "Matrifol",
        "en": "Leavanny",
        "fr": "Manternel"
      },
      543: {
        "de": "Toxiped",
        "en": "Venipede",
        "fr": "Venipatte"
      },
      544: {
        "de": "Rollum",
        "en": "Whirlipede",
        "fr": "Scobolide"
      },
      545: {
        "de": "Cerapendra",
        "en": "Scolipede",
        "fr": "Brutapode"
      },
      546: {
        "de": "Waumboll",
        "en": "Cottonee",
        "fr": "Doudouvet"
      },
      547: {
        "de": "Elfun",
        "en": "Whimsicott",
        "fr": "Farfaduvet"
      },
      548: {
        "de": "Lilminip",
        "en": "Petilil",
        "fr": "Chlorobule"
      },
      549: {
        "de": "Dressella",
        "en": "Lilligant",
        "fr": "Fragilady"
      },
      550: {
        "de": "Barschuft",
        "en": "Basculin",
        "fr": "Bargantua"
      },
      551: {
        "de": "Ganovil",
        "en": "Sandile",
        "fr": "Mascaïman"
      },
      552: {
        "de": "Rokkaiman",
        "en": "Krokorok",
        "fr": "Escroco"
      },
      553: {
        "de": "Rabigator",
        "en": "Krookodile",
        "fr": "Crocorible"
      },
      554: {
        "de": "Flampion",
        "en": "Darumaka",
        "fr": "Darumarond"
      },
      555: {
        "de": "Flampivian",
        "en": "Darmanitan",
        "fr": "Darumacho"
      },
      556: {
        "de": "Maracamba",
        "en": "Maractus",
        "fr": "Maracachi"
      },
      557: {
        "de": "Lithomith",
        "en": "Dwebble",
        "fr": "Crabicoque"
      },
      558: {
        "de": "Castellith",
        "en": "Crustle",
        "fr": "Crabaraque"
      },
      559: {
        "de": "Zurrokex",
        "en": "Scraggy",
        "fr": "Baggiguane"
      },
      560: {
        "de": "Irokex",
        "en": "Scrafty",
        "fr": "Baggaïd"
      },
      561: {
        "de": "Symvolara",
        "en": "Sigilyph",
        "fr": "Cryptéro"
      },
      562: {
        "de": "Makabaja",
        "en": "Yamask",
        "fr": "Tutafeh"
      },
      563: {
        "de": "Echnatoll",
        "en": "Cofagrigus",
        "fr": "Tutankafer"
      },
      564: {
        "de": "Galapaflos",
        "en": "Tirtouga",
        "fr": "Carapagos"
      },
      565: {
        "de": "Karippas",
        "en": "Carracosta",
        "fr": "Mégapagos"
      },
      566: {
        "de": "Flapteryx",
        "en": "Archen",
        "fr": "Arkéapti"
      },
      567: {
        "de": "Aeropteryx",
        "en": "Archeops",
        "fr": "Aéroptéryx"
      },
      568: {
        "de": "Unratütox",
        "en": "Trubbish",
        "fr": "Miamiasme"
      },
      569: {
        "de": "Deponitox",
        "en": "Garbodor",
        "fr": "Miasmax"
      },
      570: {
        "de": "Zorua",
        "en": "Zorua",
        "fr": "Zorua"
      },
      571: {
        "de": "Zoroark",
        "en": "Zoroark",
        "fr": "Zoroark"
      },
      572: {
        "de": "Picochilla",
        "en": "Minccino",
        "fr": "Chinchidou"
      },
      573: {
        "de": "Chillabell",
        "en": "Cinccino",
        "fr": "Pashmilla"
      },
      574: {
        "de": "Mollimorba",
        "en": "Gothita",
        "fr": "Scrutella"
      },
      575: {
        "de": "Hypnomorba",
        "en": "Gothorita",
        "fr": "Mesmérella"
      },
      576: {
        "de": "Morbitesse",
        "en": "Gothitelle",
        "fr": "Sidérella"
      },
      577: {
        "de": "Monozyto",
        "en": "Solosis",
        "fr": "Nucléos"
      },
      578: {
        "de": "Mitodos",
        "en": "Duosion",
        "fr": "Méios"
      },
      579: {
        "de": "Zytomega",
        "en": "Reuniclus",
        "fr": "Symbios"
      },
      580: {
        "de": "Piccolente",
        "en": "Ducklett",
        "fr": "Couaneton"
      },
      581: {
        "de": "Swaroness",
        "en": "Swanna",
        "fr": "Lakmécygne"
      },
      582: {
        "de": "Gelatini",
        "en": "Vanillite",
        "fr": "Sorbébé"
      },
      583: {
        "de": "Gelatroppo",
        "en": "Vanillish",
        "fr": "Sorboul"
      },
      584: {
        "de": "Gelatwino",
        "en": "Vanilluxe",
        "fr": "Sorbouboul"
      },
      585: {
        "de": "Sesokitz",
        "en": "Deerling",
        "fr": "Vivaldaim"
      },
      586: {
        "de": "Kronjuwild",
        "en": "Sawsbuck",
        "fr": "Haydaim"
      },
      587: {
        "de": "Emolga",
        "en": "Emolga",
        "fr": "Emolga"
      },
      588: {
        "de": "Laukaps",
        "en": "Karrablast",
        "fr": "Carabing"
      },
      589: {
        "de": "Cavalanzas",
        "en": "Escavalier",
        "fr": "Lançargot"
      },
      590: {
        "de": "Tarnpignon",
        "en": "Foongus",
        "fr": "Trompignon"
      },
      591: {
        "de": "Hutsassa",
        "en": "Amoonguss",
        "fr": "Gaulet"
      },
      592: {
        "de": "Quabbel",
        "en": "Frillish",
        "fr": "Viskuse"
      },
      593: {
        "de": "Apoquallyp",
        "en": "Jellicent",
        "fr": "Moyade"
      },
      594: {
        "de": "Mamolida",
        "en": "Alomomola",
        "fr": "Mamanbo"
      },
      595: {
        "de": "Wattzapf",
        "en": "Joltik",
        "fr": "Statitik"
      },
      596: {
        "de": "Voltula",
        "en": "Galvantula",
        "fr": "Mygavolt"
      },
      597: {
        "de": "Kastadur",
        "en": "Ferroseed",
        "fr": "Grindur"
      },
      598: {
        "de": "Tentantel",
        "en": "Ferrothorn",
        "fr": "Noacier"
      },
      599: {
        "de": "Klikk",
        "en": "Klink",
        "fr": "Tic"
      },
      600: {
        "de": "Kliklak",
        "en": "Klang",
        "fr": "Clic"
      },
      601: {
        "de": "Klikdiklak",
        "en": "Klinklang",
        "fr": "Cliticlic"
      },
      602: {
        "de": "Zapplardin",
        "en": "Tynamo",
        "fr": "Anchwatt"
      },
      603: {
        "de": "Zapplalek",
        "en": "Eelektrik",
        "fr": "Lampéroie"
      },
      604: {
        "de": "Zapplarang",
        "en": "Eelektross",
        "fr": "Ohmassacre"
      },
      605: {
        "de": "Pygraulon",
        "en": "Elgyem",
        "fr": "Lewsor"
      },
      606: {
        "de": "Megalon",
        "en": "Beheeyem",
        "fr": "Neitram"
      },
      607: {
        "de": "Lichtel",
        "en": "Litwick",
        "fr": "Funécire"
      },
      608: {
        "de": "Laternecto",
        "en": "Lampent",
        "fr": "Mélancolux"
      },
      609: {
        "de": "Skelabra",
        "en": "Chandelure",
        "fr": "Lugulabre"
      },
      610: {
        "de": "Milza",
        "en": "Axew",
        "fr": "Coupenotte"
      },
      611: {
        "de": "Sharfax",
        "en": "Fraxure",
        "fr": "Incisache"
      },
      612: {
        "de": "Maxax",
        "en": "Haxorus",
        "fr": "Tranchodon"
      },
      613: {
        "de": "Petznief",
        "en": "Cubchoo",
        "fr": "Polarhume"
      },
      614: {
        "de": "Siberio",
        "en": "Beartic",
        "fr": "Polagriffe"
      },
      615: {
        "de": "Frigometri",
        "en": "Cryogonal",
        "fr": "Hexagel"
      },
      616: {
        "de": "Schnuthelm",
        "en": "Shelmet",
        "fr": "Escargaume"
      },
      617: {
        "de": "Hydragil",
        "en": "Accelgor",
        "fr": "Limaspeed"
      },
      618: {
        "de": "Flunschlik",
        "en": "Stunfisk",
        "fr": "Limonde"
      },
      619: {
        "de": "Fu",
        "en": "Mienfoo",
        "fr": "Kungfouine"
      },
      620: {
        "de": "Shu",
        "en": "Mienshao",
        "fr": "Shaofouine"
      },
      621: {
        "de": "Shardrago",
        "en": "Druddigon",
        "fr": "Drakkarmin"
      },
      622: {
        "de": "Golbit",
        "en": "Golett",
        "fr": "Gringolem"
      },
      623: {
        "de": "Golgantes",
        "en": "Golurk",
        "fr": "Golemastoc"
      },
      624: {
        "de": "Gladiantri",
        "en": "Pawniard",
        "fr": "Scalpion"
      },
      625: {
        "de": "Caesurio",
        "en": "Bisharp",
        "fr": "Scalproie"
      },
      626: {
        "de": "Bisofank",
        "en": "Bouffalant",
        "fr": "Frison"
      },
      627: {
        "de": "Geronimatz",
        "en": "Rufflet",
        "fr": "Furaiglon"
      },
      628: {
        "de": "Washakwil",
        "en": "Braviary",
        "fr": "Gueriaigle"
      },
      629: {
        "de": "Skallyk",
        "en": "Vullaby",
        "fr": "Vostourno"
      },
      630: {
        "de": "Grypheldis",
        "en": "Mandibuzz",
        "fr": "Vaututrice"
      },
      631: {
        "de": "Furnifraß",
        "en": "Heatmor",
        "fr": "Aflamanoir"
      },
      632: {
        "de": "Fermicula",
        "en": "Durant",
        "fr": "Fermite"
      },
      633: {
        "de": "Kapuno",
        "en": "Deino",
        "fr": "Solochi"
      },
      634: {
        "de": "Duodino",
        "en": "Zweilous",
        "fr": "Diamat"
      },
      635: {
        "de": "Trikephalo",
        "en": "Hydreigon",
        "fr": "Trioxhydre"
      },
      636: {
        "de": "Ignivor",
        "en": "Larvesta",
        "fr": "Pyronille"
      },
      637: {
        "de": "Ramoth",
        "en": "Volcarona",
        "fr": "Pyrax"
      },
      638: {
        "de": "Kobalium",
        "en": "Cobalion",
        "fr": "Cobaltium"
      },
      639: {
        "de": "Terrakium",
        "en": "Terrakion",
        "fr": "Terrakium"
      },
      640: {
        "de": "Viridium",
        "en": "Virizion",
        "fr": "Viridium"
      },
      641: {
        "de": "Boreos",
        "en": "Tornadus",
        "fr": "Boréas"
      },
      642: {
        "de": "Voltolos",
        "en": "Thundurus",
        "fr": "Fulguris"
      },
      643: {
        "de": "Reshiram",
        "en": "Reshiram",
        "fr": "Reshiram"
      },
      644: {
        "de": "Zekrom",
        "en": "Zekrom",
        "fr": "Zekrom"
      },
      645: {
        "de": "Demeteros",
        "en": "Landorus",
        "fr": "Démétéros"
      },
      646: {
        "de": "Kyurem",
        "en": "Kyurem",
        "fr": "Kyurem"
      },
      647: {
        "de": "Keldeo",
        "en": "Keldeo",
        "fr": "Keldeo"
      },
      648: {
        "de": "Meloetta",
        "en": "Meloetta",
        "fr": "Meloetta"
      },
      649: {
        "de": "Genesect",
        "en": "Genesect",
        "fr": "Genesect"
      },
      650: {
        "de": "Igamaro",
        "en": "Chespin",
        "fr": "Marisson"
      },
      651: {
        "de": "Igastarnish",
        "en": "Quilladin",
        "fr": "Boguérisse"
      },
      652: {
        "de": "Brigaron",
        "en": "Chesnaught",
        "fr": "Blindépique"
      },
      653: {
        "de": "Fynx",
        "en": "Fennekin",
        "fr": "Feunnec"
      },
      654: {
        "de": "Rutena",
        "en": "Braixen",
        "fr": "Roussil"
      },
      655: {
        "de": "Fennexis",
        "en": "Delphox",
        "fr": "Goupelin"
      },
      656: {
        "de": "Froxy",
        "en": "Froakie",
        "fr": "Grenousse"
      },
      657: {
        "de": "Amphizel",
        "en": "Frogadier",
        "fr": "Croâporal"
      },
      658: {
        "de": "Quajutsu",
        "en": "Greninja",
        "fr": "Amphinobi"
      },
      659: {
        "de": "Scoppel",
        "en": "Bunnelby",
        "fr": "Sapereau"
      },
      660: {
        "de": "Grebbit",
        "en": "Diggersby",
        "fr": "Excavarenne"
      },
      661: {
        "de": "Dartiri",
        "en": "Fletchling",
        "fr": "Passerouge"
      },
      662: {
        "de": "Dartignis",
        "en": "Fletchinder",
        "fr": "Braisillon"
      },
      663: {
        "de": "Fiaro",
        "en": "Talonflame",
        "fr": "Flambusard"
      },
      664: {
        "de": "Purmel",
        "en": "Scatterbug",
        "fr": "Lépidonille"
      },
      665: {
        "de": "Puponcho",
        "en": "Spewpa",
        "fr": "Pérégrain"
      },
      666: {
        "de": "Vivillon",
        "en": "Vivillon",
        "fr": "Prismillon"
      },
      667: {
        "de": "Leufeo",
        "en": "Litleo",
        "fr": "Hélionceau"
      },
      668: {
        "de": "Pyroleo",
        "en": "Pyroar",
        "fr": "Némélios"
      },
      669: {
        "de": "Flabébé",
        "en": "Flabébé",
        "fr": "Flabébé"
      },
      670: {
        "de": "Floette",
        "en": "Floette",
        "fr": "FLOETTE"
      },
      671: {
        "de": "Florges",
        "en": "Florges",
        "fr": "Florges"
      },
      672: {
        "de": "Mähikel",
        "en": "Skiddo",
        "fr": "Cabriolaine"
      },
      673: {
        "de": "Chevrumm",
        "en": "Gogoat",
        "fr": "Chevroum"
      },
      674: {
        "de": "Pam",
        "en": "Pancham",
        "fr": "Pandespiègle"
      },
      675: {
        "de": "Pandagro",
        "en": "Pangoro",
        "fr": "Pandarbare"
      },
      676: {
        "de": "Coiffwaff",
        "en": "Furfrou",
        "fr": "Couafarel"
      },
      677: {
        "de": "Psiau",
        "en": "Espurr",
        "fr": "Psystigri"
      },
      678: {
        "de": "Psiaugon",
        "en": "Meowstic",
        "fr": "Mistigrix"
      },
      679: {
        "de": "Gramokles",
        "en": "Honedge",
        "fr": "Monorpale"
      },
      680: {
        "de": "Duokles",
        "en": "Doublade",
        "fr": "Dimoclès"
      },
      681: {
        "de": "Durengard",
        "en": "Aegislash",
        "fr": "Exagide"
      },
      682: {
        "de": "Parfi",
        "en": "Spritzee",
        "fr": "Fluvetin"
      },
      683: {
        "de": "Parfinesse",
        "en": "Aromatisse",
        "fr": "Cocotine"
      },
      684: {
        "de": "Flauschling",
        "en": "Swirlix",
        "fr": "Sucroquin"
      },
      685: {
        "de": "Sabbaione",
        "en": "Slurpuff",
        "fr": "Cupcanaille"
      },
      686: {
        "de": "Iscalar",
        "en": "Inkay",
        "fr": "Sepiatop"
      },
      687: {
        "de": "Calamanero",
        "en": "Malamar",
        "fr": "Sepiatroce"
      },
      688: {
        "de": "Bithora",
        "en": "Binacle",
        "fr": "Opermine"
      },
      689: {
        "de": "Thanathora",
        "en": "Barbaracle",
        "fr": "Golgopathe"
      },
      690: {
        "de": "Algitt",
        "en": "Skrelp",
        "fr": "Venalgue"
      },
      691: {
        "de": "Tandrak",
        "en": "Dragalge",
        "fr": "Kravarech"
      },
      692: {
        "de": "Scampisto",
        "en": "Clauncher",
        "fr": "Flingouste"
      },
      693: {
        "de": "Wummer",
        "en": "Clawitzer",
        "fr": "Gamblast"
      },
      694: {
        "de": "Eguana",
        "en": "Helioptile",
        "fr": "Galvaran"
      },
      695: {
        "de": "Elezard",
        "en": "Heliolisk",
        "fr": "Iguolta"
      },
      696: {
        "de": "Balgoras",
        "en": "Tyrunt",
        "fr": "Ptyranidur"
      },
      697: {
        "de": "Monargoras",
        "en": "Tyrantrum",
        "fr": "Rexillius"
      },
      698: {
        "de": "Amarino",
        "en": "Amaura",
        "fr": "Amagara"
      },
      699: {
        "de": "Amagarga",
        "en": "Aurorus",
        "fr": "Dragmara"
      },
      700: {
        "de": "Feelinara",
        "en": "Sylveon",
        "fr": "Nymphali"
      },
      701: {
        "de": "Resladero",
        "en": "Hawlucha",
        "fr": "Brutalibré"
      },
      702: {
        "de": "Dedenne",
        "en": "Dedenne",
        "fr": "DEDENNE"
      },
      703: {
        "de": "Rocara",
        "en": "Carbink",
        "fr": "Strassie"
      },
      704: {
        "de": "Viscora",
        "en": "Goomy",
        "fr": "Mucuscule"
      },
      705: {
        "de": "Viscargot",
        "en": "Sliggoo",
        "fr": "Colimucus"
      },
      706: {
        "de": "Viscogon",
        "en": "Goodra",
        "fr": "Muplodocus"
      },
      707: {
        "de": "Clavion",
        "en": "Klefki",
        "fr": "Trousselin"
      },
      708: {
        "de": "Paragoni",
        "en": "Phantump",
        "fr": "Brocélôme"
      },
      709: {
        "de": "Trombork",
        "en": "Trevenant",
        "fr": "Desséliande"
      },
      710: {
        "de": "Irrbis",
        "en": "Pumpkaboo",
        "fr": "Pitrouille"
      },
      711: {
        "de": "Pumpdjinn",
        "en": "Gourgeist",
        "fr": "Banshitrouye"
      },
      712: {
        "de": "Arktip",
        "en": "Bergmite",
        "fr": "Grelaçon"
      },
      713: {
        "de": "Arktilas",
        "en": "Avalugg",
        "fr": "Séracrawl"
      },
      714: {
        "de": "eF-eM",
        "en": "Noibat",
        "fr": "Sonistrelle"
      },
      715: {
        "de": "UHaFnir",
        "en": "Noivern",
        "fr": "Bruyverne"
      },
      716: {
        "de": "Xerneas",
        "en": "Xerneas",
        "fr": "Xerneas"
      },
      717: {
        "de": "Yveltal",
        "en": "Yveltal",
        "fr": "Yveltal"
      },
      718: {
        "de": "Zygarde",
        "en": "Zygarde",
        "fr": "Zygarde"
      },
      719: {
        "de": "Diancie",
        "en": "Diancie",
        "fr": "Diancie"
      },
      720: {
        "de": "Hoopa",
        "en": "Hoopa",
        "fr": "Hoopa"
      },
      721: {
        "de": "Volcanion",
        "en": "Volcanion",
        "fr": "Volcanion"
      },
      722: {
        "de": "Bauz",
        "en": "Rowlet",
        "fr": "Brindibou"
      },
      723: {
        "de": "Arboretoss",
        "en": "Dartrix",
        "fr": "Efflèche"
      },
      724: {
        "de": "Silvarro",
        "en": "Decidueye",
        "fr": "Archéduc"
      },
      725: {
        "de": "Flamiau",
        "en": "Litten",
        "fr": "Flamiaou"
      },
      726: {
        "de": "Miezunder",
        "en": "Torracat",
        "fr": "Matoufeu"
      },
      727: {
        "de": "Fuegro",
        "en": "Incineroar",
        "fr": "Félinferno"
      },
      728: {
        "de": "Robball",
        "en": "Popplio",
        "fr": "Otaquin"
      },
      729: {
        "de": "Marikeck",
        "en": "Brionne",
        "fr": "Otarlette"
      },
      730: {
        "de": "Primarene",
        "en": "Primarina",
        "fr": "Oratoria"
      },
      731: {
        "de": "Peppeck",
        "en": "Pikipek",
        "fr": "Picassaut"
      },
      732: {
        "de": "Trompeck",
        "en": "Trumbeak",
        "fr": "Piclairon"
      },
      733: {
        "de": "Tukanon",
        "en": "Toucannon",
        "fr": "Bazoucan"
      },
      734: {
        "de": "Mangunior",
        "en": "Yungoos",
        "fr": "Manglouton"
      },
      735: {
        "de": "Manguspektor",
        "en": "Gumshoos",
        "fr": "Argouste"
      },
      736: {
        "de": "Mabula",
        "en": "Grubbin",
        "fr": "Larvibule"
      },
      737: {
        "de": "Akkup",
        "en": "Charjabug",
        "fr": "Chrysapile"
      },
      738: {
        "de": "Donarion",
        "en": "Vikavolt",
        "fr": "Lucanon"
      },
      739: {
        "de": "Krabbox",
        "en": "Crabrawler",
        "fr": "Crabagarre"
      },
      740: {
        "de": "Krawell",
        "en": "Crabominable",
        "fr": "Crabominable"
      },
      741: {
        "de": "Choreogel",
        "en": "Oricorio",
        "fr": "Plumeline"
      },
      742: {
        "de": "Wommel",
        "en": "Cutiefly",
        "fr": "Bombydou"
      },
      743: {
        "de": "Bandelby",
        "en": "Ribombee",
        "fr": "Rubombelle"
      },
      744: {
        "de": "Wuffels",
        "en": "Rockruff",
        "fr": "Rocabot"
      },
      745: {
        "de": "Wolwerock",
        "en": "Lycanroc",
        "fr": "Lougaroc"
      },
      746: {
        "de": "Lusardin",
        "en": "Wishiwashi",
        "fr": "Froussardine"
      },
      747: {
        "de": "Garstella",
        "en": "Mareanie",
        "fr": "Vorastérie"
      },
      748: {
        "de": "Aggrostella",
        "en": "Toxapex",
        "fr": "Prédastérie"
      },
      749: {
        "de": "Pampuli",
        "en": "Mudbray",
        "fr": "Tiboudet"
      },
      750: {
        "de": "Pampross",
        "en": "Mudsdale",
        "fr": "Bourrinos"
      },
      751: {
        "de": "Araqua",
        "en": "Dewpider",
        "fr": "Araqua"
      },
      752: {
        "de": "Aranestro",
        "en": "Araquanid",
        "fr": "Tarenbulle"
      },
      753: {
        "de": "Imantis",
        "en": "Fomantis",
        "fr": "Mimantis"
      },
      754: {
        "de": "Mantidea",
        "en": "Lurantis",
        "fr": "Floramantis"
      },
      755: {
        "de": "Bubungus",
        "en": "Morelull",
        "fr": "Spododo"
      },
      756: {
        "de": "Lamellux",
        "en": "Shiinotic",
        "fr": "Lampignon"
      },
      757: {
        "de": "Molunk",
        "en": "Salandit",
        "fr": "Tritox"
      },
      758: {
        "de": "Amfira",
        "en": "Salazzle",
        "fr": "Malamandre"
      },
      759: {
        "de": "Velursi",
        "en": "Stufful",
        "fr": "Nounourson"
      },
      760: {
        "de": "Kosturso",
        "en": "Bewear",
        "fr": "Chelours"
      },
      761: {
        "de": "Frubberl",
        "en": "Bounsweet",
        "fr": "Croquine"
      },
      762: {
        "de": "Frubaila",
        "en": "Steenee",
        "fr": "Candine"
      },
      763: {
        "de": "Fruyal",
        "en": "Tsareena",
        "fr": "Sucreine"
      },
      764: {
        "de": "Curelei",
        "en": "Comfey",
        "fr": "Guérilande"
      },
      765: {
        "de": "Kommandutan",
        "en": "Oranguru",
        "fr": "Gouroutan"
      },
      766: {
        "de": "Quartermak",
        "en": "Passimian",
        "fr": "Quartermac"
      },
      767: {
        "de": "Reißlaus",
        "en": "Wimpod",
        "fr": "Sovkipou"
      },
      768: {
        "de": "Tectass",
        "en": "Golisopod",
        "fr": "Sarmuraï"
      },
      769: {
        "de": "Sankabuh",
        "en": "Sandygast",
        "fr": "Bacabouh"
      },
      770: {
        "de": "Colossand",
        "en": "Palossand",
        "fr": "Trépassable"
      },
      771: {
        "de": "Gufa",
        "en": "Pyukumuku",
        "fr": "Concombaffe"
      },
      772: {
        "de": "Null",
        "en": "Null",
        "fr": "NULL"
      },
      773: {
        "de": "Amigento",
        "en": "Silvally",
        "fr": "Silvallié"
      },
      774: {
        "de": "Meteno",
        "en": "Minior",
        "fr": "Météno"
      },
      775: {
        "de": "Koalelu",
        "en": "Komala",
        "fr": "Dodoala"
      },
      776: {
        "de": "Tortunator",
        "en": "Turtonator",
        "fr": "Boumata"
      },
      777: {
        "de": "Togedemaru",
        "en": "Togedemaru",
        "fr": "Togedemaru"
      },
      778: {
        "de": "Mimigma",
        "en": "Mimikyu",
        "fr": "Mimiqui"
      },
      779: {
        "de": "Knirfish",
        "en": "Bruxish",
        "fr": "Denticrisse"
      },
      780: {
        "de": "Sen-Long",
        "en": "Drampa",
        "fr": "Draïeul"
      },
      781: {
        "de": "Moruda",
        "en": "Dhelmise",
        "fr": "Sinistrail"
      },
      782: {
        "de": "Miniras",
        "en": "Jangmo-o",
        "fr": "Bébécaille"
      },
      783: {
        "de": "Mediras",
        "en": "Hakamo-o",
        "fr": "Écaïd"
      },
      784: {
        "de": "Grandiras",
        "en": "Kommo-o",
        "fr": "Ékaïser"
      },
      785: {
        "de": "Kapu-Riki",
        "en": "Tapu Koko",
        "fr": "Tokorico"
      },
      786: {
        "de": "Kapu-Fala",
        "en": "Tapu Lele",
        "fr": "Tokopiyon"
      },
      787: {
        "de": "Kapu-Toro",
        "en": "Tapu Bulu",
        "fr": "Tokotoro"
      },
      788: {
        "de": "Kapu-Kime",
        "en": "Tapu Fini",
        "fr": "Tokopisco"
      },
      789: {
        "de": "Cosmog",
        "en": "Cosmog",
        "fr": "Cosmog"
      },
      790: {
        "de": "Cosmovum",
        "en": "Cosmoem",
        "fr": "Cosmovum"
      },
      791: {
        "de": "Solgaleo",
        "en": "Solgaleo",
        "fr": "Solgaleo"
      },
      792: {
        "de": "Lunala",
        "en": "Lunala",
        "fr": "Lunala"
      },
      793: {
        "de": "Anego",
        "en": "Nihilego",
        "fr": "Zéroïd"
      },
      794: {
        "de": "Masskito",
        "en": "Buzzwole",
        "fr": "Mouscoto"
      },
      795: {
        "de": "Schabelle",
        "en": "Pheromosa",
        "fr": "Cancrelove"
      },
      796: {
        "de": "Voltriant",
        "en": "Xurkitree",
        "fr": "Câblifère"
      },
      797: {
        "de": "Kaguron",
        "en": "Celesteela",
        "fr": "Bamboiselle"
      },
      798: {
        "de": "Katagami",
        "en": "Kartana",
        "fr": "Katagami"
      },
      799: {
        "de": "Schlingking",
        "en": "Guzzlord",
        "fr": "Engloutyran"
      },
      800: {
        "de": "Necrozma",
        "en": "Necrozma",
        "fr": "Necrozma"
      },
      801: {
        "de": "Magearna",
        "en": "Magearna",
        "fr": "Magearna"
      },
      802: {
        "de": "Marshadow",
        "en": "Marshadow",
        "fr": "Marshadow"
      },
      803: {
        "de": "Venicro",
        "en": "Poipole",
        "fr": "Vémini"
      },
      804: {
        "de": "Agoyon",
        "en": "Naganadel",
        "fr": "Mandrillon"
      },
      805: {
        "de": "Muramura",
        "en": "Stakataka",
        "fr": "Ama-Ama"
      },
      806: {
        "de": "Kopplosio",
        "en": "Blacephalon",
        "fr": "Pierroteknik"
      },
      807: {
        "de": "Zeraora",
        "en": "Zeraora",
        "fr": "Zeraora"
      },
      808: {
        "de": "Meltan",
        "en": "Meltan",
        "fr": "Meltan"
      },
      809: {
        "de": "Melmetal",
        "en": "Melmetal",
        "fr": "Melmetal"
      }
    }
    self.getIV(value)
    self.getLeveFromFile(value)
    self.getModeFromFile(value)
    return switch[value][language]

  def getForm(self,value,language):
    switch = {
      ### DEFAULT VALUE
      None: {
        "de": "Form fehlt",
        "en": "",
        "fr": ""
      },
      0: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1: {
        "de": "A",
        "en": "",
        "fr": ""
      },
      2: {
        "de": "B",
        "en": "",
        "fr": ""
      },
      3: {
        "de": "C",
        "en": "",
        "fr": ""
      },
      4: {
        "de": "D",
        "en": "",
        "fr": ""
      },
      5: {
        "de": "E",
        "en": "",
        "fr": ""
      },
      6: {
        "de": "F",
        "en": "",
        "fr": ""
      },
      7: {
        "de": "G",
        "en": "",
        "fr": ""
      },
      8: {
        "de": "H",
        "en": "",
        "fr": ""
      },
      9: {
        "de": "I",
        "en": "",
        "fr": ""
      },
      10: {
        "de": "J",
        "en": "",
        "fr": ""
      },
      11: {
        "de": "K",
        "en": "",
        "fr": ""
      },
      12: {
        "de": "L",
        "en": "",
        "fr": ""
      },
      13: {
        "de": "M",
        "en": "",
        "fr": ""
      },
      14: {
        "de": "N",
        "en": "",
        "fr": ""
      },
      15: {
        "de": "O",
        "en": "",
        "fr": ""
      },
      16: {
        "de": "P",
        "en": "",
        "fr": ""
      },
      17: {
        "de": "Q",
        "en": "",
        "fr": ""
      },
      18: {
        "de": "R",
        "en": "",
        "fr": ""
      },
      19: {
        "de": "S",
        "en": "",
        "fr": ""
      },
      20: {
        "de": "T",
        "en": "",
        "fr": ""
      },
      21: {
        "de": "U",
        "en": "",
        "fr": ""
      },
      22: {
        "de": "V",
        "en": "",
        "fr": ""
      },
      23: {
        "de": "W",
        "en": "",
        "fr": ""
      },
      24: {
        "de": "X",
        "en": "",
        "fr": ""
      },
      25: {
        "de": "Y",
        "en": "",
        "fr": ""
      },
      26: {
        "de": "Z",
        "en": "",
        "fr": ""
      },
      27: {
        "de": "!",
        "en": "",
        "fr": ""
      },
      28: {
        "de": "?",
        "en": "",
        "fr": ""
      },
      29: {
        "de": "",
        "en": "",
        "fr": ""
      },
      30: {
        "de": "Sunny",
        "en": "",
        "fr": ""
      },
      31: {
        "de": "Rainy",
        "en": "",
        "fr": ""
      },
      32: {
        "de": "Snowy",
        "en": "",
        "fr": ""
      },
      33: {
        "de": "",
        "en": "",
        "fr": ""
      },
      34: {
        "de": "Attack",
        "en": "",
        "fr": ""
      },
      35: {
        "de": "Defense",
        "en": "",
        "fr": ""
      },
      36: {
        "de": "Speed",
        "en": "",
        "fr": ""
      },
      37: {
        "de": "00",
        "en": "",
        "fr": ""
      },
      38: {
        "de": "01",
        "en": "",
        "fr": ""
      },
      39: {
        "de": "02",
        "en": "",
        "fr": ""
      },
      40: {
        "de": "03",
        "en": "",
        "fr": ""
      },
      41: {
        "de": "04",
        "en": "",
        "fr": ""
      },
      42: {
        "de": "05",
        "en": "",
        "fr": ""
      },
      43: {
        "de": "06",
        "en": "",
        "fr": ""
      },
      44: {
        "de": "07",
        "en": "",
        "fr": ""
      },
      45: {
        "de": "",
        "en": "",
        "fr": ""
      },
      46: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      47: {
        "de": "",
        "en": "",
        "fr": ""
      },
      48: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      49: {
        "de": "",
        "en": "",
        "fr": ""
      },
      50: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      51: {
        "de": "",
        "en": "",
        "fr": ""
      },
      52: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      53: {
        "de": "",
        "en": "",
        "fr": ""
      },
      54: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      55: {
        "de": "",
        "en": "",
        "fr": ""
      },
      56: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      57: {
        "de": "",
        "en": "",
        "fr": ""
      },
      58: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      59: {
        "de": "",
        "en": "",
        "fr": ""
      },
      60: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      61: {
        "de": "",
        "en": "",
        "fr": ""
      },
      62: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      63: {
        "de": "",
        "en": "",
        "fr": ""
      },
      64: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      65: {
        "de": "",
        "en": "",
        "fr": ""
      },
      66: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      67: {
        "de": "",
        "en": "",
        "fr": ""
      },
      68: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      69: {
        "de": "",
        "en": "",
        "fr": ""
      },
      70: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      71: {
        "de": "",
        "en": "",
        "fr": ""
      },
      72: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      73: {
        "de": "",
        "en": "",
        "fr": ""
      },
      74: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      75: {
        "de": "",
        "en": "",
        "fr": ""
      },
      76: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      77: {
        "de": "",
        "en": "",
        "fr": ""
      },
      78: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      79: {
        "de": "",
        "en": "",
        "fr": ""
      },
      80: {
        "de": "Alola",
        "en": "",
        "fr": ""
      },
      81: {
        "de": "",
        "en": "",
        "fr": ""
      },
      82: {
        "de": "Frost",
        "en": "",
        "fr": ""
      },
      83: {
        "de": "Fan",
        "en": "",
        "fr": ""
      },
      84: {
        "de": "Mow",
        "en": "",
        "fr": ""
      },
      85: {
        "de": "Wash",
        "en": "",
        "fr": ""
      },
      86: {
        "de": "Heat",
        "en": "",
        "fr": ""
      },
      87: {
        "de": "Plant",
        "en": "",
        "fr": ""
      },
      88: {
        "de": "Sandy",
        "en": "",
        "fr": ""
      },
      89: {
        "de": "Trash",
        "en": "",
        "fr": ""
      },
      90: {
        "de": "Altered",
        "en": "",
        "fr": ""
      },
      91: {
        "de": "Origin",
        "en": "",
        "fr": ""
      },
      92: {
        "de": "Sky",
        "en": "",
        "fr": ""
      },
      93: {
        "de": "Land",
        "en": "",
        "fr": ""
      },
      94: {
        "de": "Overcast",
        "en": "",
        "fr": ""
      },
      95: {
        "de": "Sunny",
        "en": "",
        "fr": ""
      },
      96: {
        "de": "West Sea",
        "en": "",
        "fr": ""
      },
      97: {
        "de": "East Sea",
        "en": "",
        "fr": ""
      },
      98: {
        "de": "West Sea",
        "en": "",
        "fr": ""
      },
      99: {
        "de": "East Sea",
        "en": "",
        "fr": ""
      },
      100: {
        "de": "",
        "en": "",
        "fr": ""
      },
      101: {
        "de": "Fighting",
        "en": "",
        "fr": ""
      },
      102: {
        "de": "Flying",
        "en": "",
        "fr": ""
      },
      103: {
        "de": "Poison",
        "en": "",
        "fr": ""
      },
      104: {
        "de": "Ground",
        "en": "",
        "fr": ""
      },
      105: {
        "de": "Rock",
        "en": "",
        "fr": ""
      },
      106: {
        "de": "Bug",
        "en": "",
        "fr": ""
      },
      107: {
        "de": "Ghost",
        "en": "",
        "fr": ""
      },
      108: {
        "de": "Steel",
        "en": "",
        "fr": ""
      },
      109: {
        "de": "Fire",
        "en": "",
        "fr": ""
      },
      110: {
        "de": "Water",
        "en": "",
        "fr": ""
      },
      111: {
        "de": "Grass",
        "en": "",
        "fr": ""
      },
      112: {
        "de": "Electric",
        "en": "",
        "fr": ""
      },
      113: {
        "de": "Psychic",
        "en": "",
        "fr": ""
      },
      114: {
        "de": "Ice",
        "en": "",
        "fr": ""
      },
      115: {
        "de": "Dragon",
        "en": "",
        "fr": ""
      },
      116: {
        "de": "Dark",
        "en": "",
        "fr": ""
      },
      117: {
        "de": "Fairy",
        "en": "",
        "fr": ""
      },
      118: {
        "de": "Plant",
        "en": "",
        "fr": ""
      },
      119: {
        "de": "Sandy",
        "en": "",
        "fr": ""
      },
      120: {
        "de": "Trash",
        "en": "",
        "fr": ""
      },
      121: {
        "de": "08",
        "en": "",
        "fr": ""
      },
      122: {
        "de": "09",
        "en": "",
        "fr": ""
      },
      123: {
        "de": "10",
        "en": "",
        "fr": ""
      },
      124: {
        "de": "11",
        "en": "",
        "fr": ""
      },
      125: {
        "de": "12",
        "en": "",
        "fr": ""
      },
      126: {
        "de": "13",
        "en": "",
        "fr": ""
      },
      127: {
        "de": "14",
        "en": "",
        "fr": ""
      },
      128: {
        "de": "15",
        "en": "",
        "fr": ""
      },
      129: {
        "de": "16",
        "en": "",
        "fr": ""
      },
      130: {
        "de": "17",
        "en": "",
        "fr": ""
      },
      131: {
        "de": "18",
        "en": "",
        "fr": ""
      },
      132: {
        "de": "19",
        "en": "",
        "fr": ""
      },
      133: {
        "de": "A",
        "en": "",
        "fr": ""
      },
      135: {
        "de": "",
        "en": "",
        "fr": ""
      },
      136: {
        "de": "Red Striped",
        "en": "",
        "fr": ""
      },
      137: {
        "de": "Blue Stripped",
        "en": "",
        "fr": ""
      },
      138: {
        "de": "Standard",
        "en": "",
        "fr": ""
      },
      139: {
        "de": "Zen",
        "en": "",
        "fr": ""
      },
      140: {
        "de": "Incarnate",
        "en": "",
        "fr": ""
      },
      141: {
        "de": "Therian",
        "en": "",
        "fr": ""
      },
      142: {
        "de": "Incarnate",
        "en": "",
        "fr": ""
      },
      143: {
        "de": "Therian",
        "en": "",
        "fr": ""
      },
      144: {
        "de": "Incarnate",
        "en": "",
        "fr": ""
      },
      145: {
        "de": "Therian",
        "en": "",
        "fr": ""
      },
      146: {
        "de": "",
        "en": "",
        "fr": ""
      },
      147: {
        "de": "Black",
        "en": "",
        "fr": ""
      },
      148: {
        "de": "White",
        "en": "",
        "fr": ""
      },
      149: {
        "de": "Ordinary",
        "en": "",
        "fr": ""
      },
      150: {
        "de": "Resolute",
        "en": "",
        "fr": ""
      },
      151: {
        "de": "Aria",
        "en": "",
        "fr": ""
      },
      152: {
        "de": "Piroutte",
        "en": "",
        "fr": ""
      },
      153: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      154: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      155: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      156: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      157: {
        "de": "",
        "en": "",
        "fr": ""
      },
      158: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      159: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      160: {
        "de": "",
        "en": "",
        "fr": ""
      },
      161: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      162: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      163: {
        "de": "",
        "en": "",
        "fr": ""
      },
      164: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      165: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      166: {
        "de": "",
        "en": "",
        "fr": ""
      },
      167: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      168: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      169: {
        "de": "",
        "en": "",
        "fr": ""
      },
      170: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      171: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      172: {
        "de": "",
        "en": "",
        "fr": ""
      },
      173: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      174: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      175: {
        "de": "",
        "en": "",
        "fr": ""
      },
      176: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      177: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      178: {
        "de": "",
        "en": "",
        "fr": ""
      },
      179: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      180: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      181: {
        "de": "",
        "en": "",
        "fr": ""
      },
      182: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      183: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      184: {
        "de": "",
        "en": "",
        "fr": ""
      },
      185: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      186: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      187: {
        "de": "",
        "en": "",
        "fr": ""
      },
      188: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      189: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      190: {
        "de": "",
        "en": "",
        "fr": ""
      },
      191: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      192: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      193: {
        "de": "",
        "en": "",
        "fr": ""
      },
      194: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      195: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      196: {
        "de": "",
        "en": "",
        "fr": ""
      },
      197: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      198: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      199: {
        "de": "",
        "en": "",
        "fr": ""
      },
      200: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      201: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      202: {
        "de": "",
        "en": "",
        "fr": ""
      },
      203: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      204: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      205: {
        "de": "",
        "en": "",
        "fr": ""
      },
      206: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      207: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      208: {
        "de": "",
        "en": "",
        "fr": ""
      },
      209: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      210: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      211: {
        "de": "",
        "en": "",
        "fr": ""
      },
      212: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      213: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      214: {
        "de": "",
        "en": "",
        "fr": ""
      },
      215: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      216: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      217: {
        "de": "",
        "en": "",
        "fr": ""
      },
      218: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      219: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      220: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      221: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      222: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      223: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      224: {
        "de": "",
        "en": "",
        "fr": ""
      },
      225: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      226: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      227: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      228: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      229: {
        "de": "",
        "en": "",
        "fr": ""
      },
      230: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      231: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      232: {
        "de": "",
        "en": "",
        "fr": ""
      },
      233: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      234: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      235: {
        "de": "",
        "en": "",
        "fr": ""
      },
      236: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      237: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      238: {
        "de": "",
        "en": "",
        "fr": ""
      },
      239: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      240: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      241: {
        "de": "",
        "en": "",
        "fr": ""
      },
      242: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      243: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      244: {
        "de": "",
        "en": "",
        "fr": ""
      },
      245: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      246: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      247: {
        "de": "",
        "en": "",
        "fr": ""
      },
      248: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      249: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      250: {
        "de": "",
        "en": "",
        "fr": ""
      },
      251: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      252: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      253: {
        "de": "",
        "en": "",
        "fr": ""
      },
      254: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      255: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      256: {
        "de": "",
        "en": "",
        "fr": ""
      },
      257: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      258: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      259: {
        "de": "",
        "en": "",
        "fr": ""
      },
      260: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      261: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      262: {
        "de": "",
        "en": "",
        "fr": ""
      },
      263: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      264: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      265: {
        "de": "",
        "en": "",
        "fr": ""
      },
      266: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      267: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      268: {
        "de": "",
        "en": "",
        "fr": ""
      },
      269: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      270: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      271: {
        "de": "",
        "en": "",
        "fr": ""
      },
      272: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      273: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      274: {
        "de": "",
        "en": "",
        "fr": ""
      },
      275: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      276: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      277: {
        "de": "",
        "en": "",
        "fr": ""
      },
      278: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      279: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      280: {
        "de": "",
        "en": "",
        "fr": ""
      },
      281: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      282: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      283: {
        "de": "",
        "en": "",
        "fr": ""
      },
      284: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      285: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      286: {
        "de": "",
        "en": "",
        "fr": ""
      },
      287: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      288: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      289: {
        "de": "",
        "en": "",
        "fr": ""
      },
      290: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      291: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      292: {
        "de": "",
        "en": "",
        "fr": ""
      },
      293: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      294: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      295: {
        "de": "",
        "en": "",
        "fr": ""
      },
      296: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      297: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      298: {
        "de": "",
        "en": "",
        "fr": ""
      },
      299: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      300: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      301: {
        "de": "",
        "en": "",
        "fr": ""
      },
      302: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      303: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      304: {
        "de": "",
        "en": "",
        "fr": ""
      },
      305: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      306: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      307: {
        "de": "",
        "en": "",
        "fr": ""
      },
      308: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      309: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      310: {
        "de": "",
        "en": "",
        "fr": ""
      },
      311: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      312: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      313: {
        "de": "",
        "en": "",
        "fr": ""
      },
      314: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      315: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      316: {
        "de": "",
        "en": "",
        "fr": ""
      },
      317: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      318: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      319: {
        "de": "",
        "en": "",
        "fr": ""
      },
      320: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      321: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      322: {
        "de": "",
        "en": "",
        "fr": ""
      },
      323: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      324: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      585: {
        "de": "Spring",
        "en": "",
        "fr": ""
      },
      586: {
        "de": "Summer",
        "en": "",
        "fr": ""
      },
      587: {
        "de": "Autumn",
        "en": "",
        "fr": ""
      },
      588: {
        "de": "Winter",
        "en": "",
        "fr": ""
      },
      589: {
        "de": "Spring",
        "en": "",
        "fr": ""
      },
      590: {
        "de": "Summer",
        "en": "",
        "fr": ""
      },
      591: {
        "de": "Autumn",
        "en": "",
        "fr": ""
      },
      592: {
        "de": "Winter",
        "en": "",
        "fr": ""
      },
      593: {
        "de": "",
        "en": "",
        "fr": ""
      },
      594: {
        "de": "SHOCK",
        "en": "",
        "fr": ""
      },
      595: {
        "de": "BURN",
        "en": "",
        "fr": ""
      },
      596: {
        "de": "CHILL",
        "en": "",
        "fr": ""
      },
      597: {
        "de": "DOUSE",
        "en": "",
        "fr": ""
      },
      598: {
        "de": "",
        "en": "",
        "fr": ""
      },
      600: {
        "de": "",
        "en": "",
        "fr": ""
      },
      602: {
        "de": "",
        "en": "",
        "fr": ""
      },
      610: {
        "de": "",
        "en": "",
        "fr": ""
      },
      611: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      612: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      613: {
        "de": "",
        "en": "",
        "fr": ""
      },
      614: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      615: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      616: {
        "de": "",
        "en": "",
        "fr": ""
      },
      617: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      618: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      619: {
        "de": "",
        "en": "",
        "fr": ""
      },
      620: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      621: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      622: {
        "de": "",
        "en": "",
        "fr": ""
      },
      623: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      624: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      625: {
        "de": "",
        "en": "",
        "fr": ""
      },
      626: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      627: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      628: {
        "de": "",
        "en": "",
        "fr": ""
      },
      629: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      630: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      631: {
        "de": "",
        "en": "",
        "fr": ""
      },
      632: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      633: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      634: {
        "de": "",
        "en": "",
        "fr": ""
      },
      635: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      636: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      637: {
        "de": "",
        "en": "",
        "fr": ""
      },
      638: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      639: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      640: {
        "de": "",
        "en": "",
        "fr": ""
      },
      641: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      642: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      643: {
        "de": "",
        "en": "",
        "fr": ""
      },
      644: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      645: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      646: {
        "de": "",
        "en": "",
        "fr": ""
      },
      647: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      648: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      649: {
        "de": "",
        "en": "",
        "fr": ""
      },
      650: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      651: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      652: {
        "de": "",
        "en": "",
        "fr": ""
      },
      653: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      654: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      655: {
        "de": "",
        "en": "",
        "fr": ""
      },
      656: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      657: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      658: {
        "de": "",
        "en": "",
        "fr": ""
      },
      659: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      660: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      661: {
        "de": "",
        "en": "",
        "fr": ""
      },
      662: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      663: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      664: {
        "de": "",
        "en": "",
        "fr": ""
      },
      665: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      666: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      667: {
        "de": "",
        "en": "",
        "fr": ""
      },
      668: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      669: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      670: {
        "de": "",
        "en": "",
        "fr": ""
      },
      671: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      672: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      673: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      674: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      675: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      676: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      677: {
        "de": "",
        "en": "",
        "fr": ""
      },
      678: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      679: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      680: {
        "de": "",
        "en": "",
        "fr": ""
      },
      681: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      682: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      683: {
        "de": "",
        "en": "",
        "fr": ""
      },
      684: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      685: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      686: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      687: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      688: {
        "de": "",
        "en": "",
        "fr": ""
      },
      689: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      690: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      691: {
        "de": "",
        "en": "",
        "fr": ""
      },
      692: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      693: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      694: {
        "de": "",
        "en": "",
        "fr": ""
      },
      695: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      696: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      697: {
        "de": "",
        "en": "",
        "fr": ""
      },
      698: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      699: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      700: {
        "de": "",
        "en": "",
        "fr": ""
      },
      701: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      702: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      703: {
        "de": "",
        "en": "",
        "fr": ""
      },
      704: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      705: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      706: {
        "de": "",
        "en": "",
        "fr": ""
      },
      707: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      708: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      709: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      710: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      711: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      712: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      713: {
        "de": "",
        "en": "",
        "fr": ""
      },
      714: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      715: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      716: {
        "de": "",
        "en": "",
        "fr": ""
      },
      717: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      718: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      719: {
        "de": "",
        "en": "",
        "fr": ""
      },
      720: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      721: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      722: {
        "de": "",
        "en": "",
        "fr": ""
      },
      723: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      724: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      725: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      726: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      727: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      728: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      729: {
        "de": "",
        "en": "",
        "fr": ""
      },
      730: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      731: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      732: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      733: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      734: {
        "de": "",
        "en": "",
        "fr": ""
      },
      735: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      736: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      737: {
        "de": "",
        "en": "",
        "fr": ""
      },
      738: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      739: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      740: {
        "de": "",
        "en": "",
        "fr": ""
      },
      741: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      742: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      743: {
        "de": "",
        "en": "",
        "fr": ""
      },
      744: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      745: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      746: {
        "de": "",
        "en": "",
        "fr": ""
      },
      747: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      748: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      749: {
        "de": "",
        "en": "",
        "fr": ""
      },
      750: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      751: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      752: {
        "de": "",
        "en": "",
        "fr": ""
      },
      753: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      754: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      755: {
        "de": "",
        "en": "",
        "fr": ""
      },
      756: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      757: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      758: {
        "de": "",
        "en": "",
        "fr": ""
      },
      759: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      760: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      761: {
        "de": "",
        "en": "",
        "fr": ""
      },
      762: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      763: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      764: {
        "de": "",
        "en": "",
        "fr": ""
      },
      765: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      766: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      767: {
        "de": "",
        "en": "",
        "fr": ""
      },
      768: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      769: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      770: {
        "de": "",
        "en": "",
        "fr": ""
      },
      771: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      772: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      773: {
        "de": "",
        "en": "",
        "fr": ""
      },
      774: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      775: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      776: {
        "de": "",
        "en": "",
        "fr": ""
      },
      777: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      778: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      779: {
        "de": "",
        "en": "",
        "fr": ""
      },
      780: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      781: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      782: {
        "de": "",
        "en": "",
        "fr": ""
      },
      783: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      784: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      785: {
        "de": "",
        "en": "",
        "fr": ""
      },
      786: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      787: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      788: {
        "de": "",
        "en": "",
        "fr": ""
      },
      789: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      790: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      791: {
        "de": "",
        "en": "",
        "fr": ""
      },
      792: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      793: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      794: {
        "de": "",
        "en": "",
        "fr": ""
      },
      795: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      796: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      797: {
        "de": "",
        "en": "",
        "fr": ""
      },
      798: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      799: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      800: {
        "de": "",
        "en": "",
        "fr": ""
      },
      801: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      802: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      803: {
        "de": "",
        "en": "",
        "fr": ""
      },
      804: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      805: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      806: {
        "de": "",
        "en": "",
        "fr": ""
      },
      807: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      808: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      809: {
        "de": "",
        "en": "",
        "fr": ""
      },
      810: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      811: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      812: {
        "de": "",
        "en": "",
        "fr": ""
      },
      813: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      814: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      815: {
        "de": "",
        "en": "",
        "fr": ""
      },
      816: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      817: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      818: {
        "de": "",
        "en": "",
        "fr": ""
      },
      819: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      820: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      821: {
        "de": "",
        "en": "",
        "fr": ""
      },
      822: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      823: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      824: {
        "de": "",
        "en": "",
        "fr": ""
      },
      825: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      826: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      827: {
        "de": "",
        "en": "",
        "fr": ""
      },
      828: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      829: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      830: {
        "de": "",
        "en": "",
        "fr": ""
      },
      831: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      832: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      833: {
        "de": "",
        "en": "",
        "fr": ""
      },
      834: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      835: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      836: {
        "de": "",
        "en": "",
        "fr": ""
      },
      837: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      838: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      839: {
        "de": "",
        "en": "",
        "fr": ""
      },
      840: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      841: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      842: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      843: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      844: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      845: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      846: {
        "de": "",
        "en": "",
        "fr": ""
      },
      847: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      848: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      849: {
        "de": "",
        "en": "",
        "fr": ""
      },
      850: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      851: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      852: {
        "de": "",
        "en": "",
        "fr": ""
      },
      853: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      854: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      855: {
        "de": "",
        "en": "",
        "fr": ""
      },
      856: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      857: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      858: {
        "de": "",
        "en": "",
        "fr": ""
      },
      859: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      860: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      861: {
        "de": "",
        "en": "",
        "fr": ""
      },
      862: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      863: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      864: {
        "de": "",
        "en": "",
        "fr": ""
      },
      865: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      866: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      867: {
        "de": "",
        "en": "",
        "fr": ""
      },
      868: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      869: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      870: {
        "de": "",
        "en": "",
        "fr": ""
      },
      871: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      872: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      873: {
        "de": "",
        "en": "",
        "fr": ""
      },
      874: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      875: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      876: {
        "de": "",
        "en": "",
        "fr": ""
      },
      877: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      878: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      879: {
        "de": "",
        "en": "",
        "fr": ""
      },
      880: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      881: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      882: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      883: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      884: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      885: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      886: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      887: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      888: {
        "de": "",
        "en": "",
        "fr": ""
      },
      889: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      890: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      891: {
        "de": "",
        "en": "",
        "fr": ""
      },
      892: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      893: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      894: {
        "de": "Fall 2019",
        "en": "",
        "fr": ""
      },
      895: {
        "de": "Fall 2019",
        "en": "",
        "fr": ""
      },
      896: {
        "de": "Fall 2019",
        "en": "",
        "fr": ""
      },
      897: {
        "de": "Fall 2019",
        "en": "",
        "fr": ""
      },
      898: {
        "de": "",
        "en": "",
        "fr": ""
      },
      899: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      900: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      901: {
        "de": "VS 2019",
        "en": "",
        "fr": ""
      },
      902: {
        "de": "",
        "en": "",
        "fr": ""
      },
      903: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      904: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      905: {
        "de": "",
        "en": "",
        "fr": ""
      },
      906: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      907: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      908: {
        "de": "",
        "en": "",
        "fr": ""
      },
      909: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      910: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      911: {
        "de": "",
        "en": "",
        "fr": ""
      },
      912: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      913: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      914: {
        "de": "",
        "en": "",
        "fr": ""
      },
      915: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      916: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      917: {
        "de": "",
        "en": "",
        "fr": ""
      },
      918: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      919: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      920: {
        "de": "",
        "en": "",
        "fr": ""
      },
      921: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      922: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      923: {
        "de": "",
        "en": "",
        "fr": ""
      },
      924: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      925: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      926: {
        "de": "",
        "en": "",
        "fr": ""
      },
      927: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      928: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      929: {
        "de": "",
        "en": "",
        "fr": ""
      },
      930: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      931: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      932: {
        "de": "",
        "en": "",
        "fr": ""
      },
      933: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      934: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      935: {
        "de": "",
        "en": "",
        "fr": ""
      },
      936: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      937: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      938: {
        "de": "",
        "en": "",
        "fr": ""
      },
      939: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      940: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      941: {
        "de": "",
        "en": "",
        "fr": ""
      },
      942: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      943: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      944: {
        "de": "Galarian",
        "en": "",
        "fr": ""
      },
      945: {
        "de": "",
        "en": "",
        "fr": ""
      },
      946: {
        "de": "Galarian",
        "en": "",
        "fr": ""
      },
      947: {
        "de": "",
        "en": "",
        "fr": ""
      },
      948: {
        "de": "Galarian",
        "en": "",
        "fr": ""
      },
      949: {
        "de": "Clone 2019",
        "en": "",
        "fr": ""
      },
      950: {
        "de": "Clone 2019",
        "en": "",
        "fr": ""
      },
      951: {
        "de": "Clone 2019",
        "en": "",
        "fr": ""
      },
      952: {
        "de": "Clone 2019",
        "en": "",
        "fr": ""
      },
      953: {
        "de": "",
        "en": "",
        "fr": ""
      },
      954: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      955: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      956: {
        "de": "",
        "en": "",
        "fr": ""
      },
      957: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      958: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      959: {
        "de": "",
        "en": "",
        "fr": ""
      },
      960: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      961: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      962: {
        "de": "",
        "en": "",
        "fr": ""
      },
      963: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      964: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      965: {
        "de": "",
        "en": "",
        "fr": ""
      },
      966: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      967: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      968: {
        "de": "",
        "en": "",
        "fr": ""
      },
      969: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      970: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      971: {
        "de": "",
        "en": "",
        "fr": ""
      },
      972: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      973: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      974: {
        "de": "",
        "en": "",
        "fr": ""
      },
      975: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      976: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      977: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      978: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      979: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      980: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      981: {
        "de": "",
        "en": "",
        "fr": ""
      },
      982: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      983: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      984: {
        "de": "",
        "en": "",
        "fr": ""
      },
      985: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      986: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      987: {
        "de": "",
        "en": "",
        "fr": ""
      },
      988: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      989: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      990: {
        "de": "",
        "en": "",
        "fr": ""
      },
      991: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      992: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      993: {
        "de": "",
        "en": "",
        "fr": ""
      },
      994: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      995: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      996: {
        "de": "",
        "en": "",
        "fr": ""
      },
      997: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      998: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      999: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1000: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1001: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1002: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1003: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1004: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1005: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1006: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1007: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1008: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1009: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1010: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1011: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1012: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1013: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1014: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1015: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1016: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1017: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1018: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1019: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1020: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1021: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1022: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1023: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1024: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1025: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1026: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1027: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1028: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1029: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1030: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1031: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1032: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1033: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1034: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1035: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1036: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1037: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1038: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1039: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1040: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1041: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1042: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1043: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1044: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1045: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1046: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1047: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1048: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1049: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1050: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1051: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1052: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1053: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1054: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1055: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1056: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1057: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1058: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1059: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1060: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1061: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1062: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1063: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1064: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1065: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1066: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1067: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1068: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1069: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1070: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1071: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1072: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1073: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1074: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1075: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1076: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1077: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1078: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1079: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1080: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1081: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1082: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1083: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1084: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1085: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1086: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1087: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1088: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1089: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1090: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1091: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1092: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1093: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1094: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1095: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1096: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1097: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1098: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1099: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1100: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1101: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1102: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1103: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1104: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1105: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1106: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1107: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1108: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1109: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1110: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1111: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1112: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1113: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1114: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1115: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1116: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1117: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1118: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1119: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1120: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1121: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1122: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1123: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1124: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1125: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1126: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1127: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1128: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1129: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1130: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1131: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1132: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1133: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1134: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1135: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1136: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1137: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1138: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1139: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1140: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1141: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1142: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1143: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1144: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1145: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1146: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1147: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1148: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1149: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1150: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1151: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1152: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1153: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1154: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1155: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1156: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1157: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1158: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1159: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1160: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1161: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1162: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1163: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1164: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1165: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1166: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1167: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1168: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1169: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1170: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1171: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1172: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1173: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1174: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1175: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1176: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1177: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1178: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1179: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1180: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1181: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1182: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1183: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1184: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1185: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1186: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1187: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1188: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1189: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1190: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1191: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1192: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1193: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1194: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1195: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1196: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1197: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1198: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1199: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1200: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1201: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1202: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1203: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1204: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1205: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1206: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1207: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1208: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1209: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1210: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1211: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1212: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1213: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1214: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1215: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1216: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1217: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1218: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1219: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1220: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1221: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1222: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1223: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1224: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1225: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1226: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1227: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1228: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1229: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1230: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1231: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1232: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1233: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1234: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1235: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1236: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1237: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1238: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1239: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1240: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1241: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1242: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1243: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1244: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1245: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1246: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1247: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1248: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1249: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1250: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1251: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1252: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1253: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1254: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1255: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1256: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1257: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1258: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1259: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1260: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1261: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1262: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1263: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1264: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1265: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1266: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1267: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1268: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1269: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1270: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1271: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1272: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1273: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1274: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1275: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1276: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1277: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1278: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1279: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1280: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1281: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1282: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1283: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1284: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1285: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1286: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1287: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1288: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1289: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1290: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1291: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1292: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1293: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1294: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1295: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1296: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1297: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1298: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1299: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1300: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1301: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1302: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1303: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1304: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1305: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1306: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1307: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1308: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1309: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1310: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1311: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1312: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1313: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1314: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1315: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1316: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1317: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1318: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1319: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1320: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1321: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1322: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1323: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1324: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1325: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1326: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1327: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1328: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1329: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1330: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1331: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1332: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1333: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1334: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1335: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1336: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1337: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1338: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1339: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1340: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1341: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1342: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1343: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1344: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1345: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1346: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1347: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1348: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1349: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1350: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1351: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1352: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1353: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1354: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1355: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1356: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1357: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1358: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1359: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1360: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1361: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1362: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1363: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1364: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1365: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1366: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1367: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1368: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1369: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1370: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1371: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1372: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1373: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1374: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1375: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1376: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1377: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1378: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1379: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1380: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1381: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1382: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1383: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1384: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1385: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1386: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1387: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1388: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1389: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1390: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1391: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1392: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1393: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1394: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1395: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1396: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1397: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1398: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1399: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1400: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1401: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1402: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1403: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1404: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1405: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1406: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1407: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1408: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1409: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1410: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1411: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1412: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1413: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1414: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1415: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1416: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1417: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1418: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1419: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1420: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1421: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1422: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1423: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1424: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1425: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1426: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1427: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1428: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1429: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1430: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1431: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1432: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1433: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1434: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1435: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1436: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1437: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1438: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1439: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1440: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1441: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1442: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1443: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1444: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1445: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1446: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1447: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1448: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1449: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1450: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1451: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1452: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1453: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1454: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1455: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1456: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1457: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1458: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1459: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1460: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1461: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1462: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1463: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1464: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1465: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1466: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1467: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1468: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1469: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1470: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1471: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1472: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1473: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1474: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1475: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1476: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1477: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1478: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1479: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1480: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1481: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1482: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1483: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1484: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1485: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1486: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1487: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1488: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1489: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1490: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1491: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1492: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1493: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1494: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1495: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1496: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1497: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1498: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1499: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1500: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1501: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1502: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1503: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1504: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1505: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1506: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1507: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1508: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1509: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1510: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1511: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1512: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1513: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1514: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1515: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1516: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1517: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1518: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1519: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1520: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1521: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1522: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1523: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1524: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1525: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1526: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1527: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1528: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1529: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1530: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1531: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1532: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1533: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1534: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1535: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1536: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1537: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1538: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1539: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1540: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1541: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1542: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1543: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1544: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1545: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1546: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1547: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1548: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1549: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1550: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1551: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1552: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1553: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1554: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1555: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1556: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1557: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1558: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1559: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1560: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1561: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1562: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1563: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1564: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1565: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1566: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1567: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1568: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1569: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1570: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1571: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1572: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1573: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1574: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1575: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1576: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1577: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1578: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1579: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1580: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1581: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1582: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1583: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1584: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1585: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1586: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1587: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1588: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1589: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1590: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1591: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1592: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1593: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1594: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1595: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1596: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1597: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1598: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1599: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1600: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1601: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1602: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1603: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1604: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1605: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1606: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1607: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1608: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1609: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1610: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1611: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1612: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1613: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1614: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1615: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1616: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1617: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1618: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1619: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1620: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1621: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1622: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1623: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1624: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1625: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1626: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1627: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1628: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1629: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1630: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1631: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1632: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1633: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1634: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1635: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1636: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1637: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1638: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1639: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1640: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1641: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1642: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1643: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1644: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1645: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1646: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1647: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1648: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1649: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1650: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1651: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1652: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1653: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1654: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1655: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1656: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1657: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1658: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1659: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1660: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1661: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1662: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1663: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1664: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1665: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1666: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1667: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1668: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1669: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1670: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1671: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1672: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1673: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1674: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1675: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1676: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1677: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1678: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1679: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1680: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1681: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1682: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1683: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1684: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1685: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1686: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1687: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1688: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1689: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1690: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1691: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1692: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1693: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1694: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1695: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1696: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1697: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1698: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1699: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1700: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1701: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1702: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1703: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1704: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1705: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1706: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1707: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1708: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1709: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1710: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1711: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1712: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1713: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1714: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1715: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1716: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1717: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1718: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1719: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1720: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1721: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1722: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1723: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1724: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1725: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1726: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1727: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1728: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1729: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1730: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1731: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1732: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1733: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1734: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1735: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1736: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1737: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1738: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1739: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1740: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1741: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1742: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1743: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1744: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1745: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1746: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1747: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1748: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1749: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1750: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1751: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1752: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1753: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1754: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1755: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1756: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1757: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1758: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1759: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1760: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1761: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1762: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1763: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1764: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1765: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1766: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1767: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1768: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1769: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1770: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1771: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1772: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1773: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1774: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1775: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1776: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1777: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1778: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1779: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1780: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1781: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1782: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1783: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1784: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1785: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1786: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1787: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1788: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1789: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1790: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1791: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1792: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1793: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1794: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1795: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1796: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1797: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1798: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1799: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1800: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1801: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1802: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1803: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1804: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1805: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1806: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1807: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1808: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1809: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1810: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1811: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1812: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1813: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1814: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1815: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1816: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1817: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1818: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1819: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1820: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1821: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1822: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1823: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1824: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1825: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1826: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1827: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1828: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1829: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1830: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1831: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1832: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1833: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1834: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1835: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1836: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1837: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1838: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1839: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1840: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1841: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1842: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1843: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1844: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1845: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1846: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1847: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1848: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1849: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1850: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1851: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1852: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1853: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1854: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1855: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1856: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1857: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1858: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1859: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1860: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1861: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1862: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1863: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1864: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1865: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1866: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1867: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1868: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1869: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1870: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1871: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1872: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1873: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1874: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1875: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1876: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1877: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1878: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1879: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1880: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1881: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1882: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1883: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1884: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1885: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1886: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1887: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1888: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1889: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1890: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1891: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1892: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1893: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1894: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1895: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1896: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1897: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1898: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1899: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1900: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1901: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1902: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1903: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1904: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1905: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1906: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1907: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1908: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1909: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1910: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1911: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1912: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1913: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1914: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1915: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1916: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1917: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1918: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1919: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1920: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1921: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1922: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1923: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1924: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1925: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1926: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1927: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1928: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1929: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1930: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1931: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1932: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1933: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1934: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1935: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1936: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1937: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1938: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1939: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1940: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1941: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1942: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1943: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1944: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1945: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1946: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1947: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1948: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1949: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1950: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1951: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1952: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1953: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1954: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1955: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1956: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1957: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1958: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1959: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1960: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1961: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1962: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1963: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1964: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1965: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1966: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1967: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1968: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1969: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1970: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1971: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1972: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1973: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1974: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1975: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1976: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1977: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1978: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1979: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1980: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1981: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1982: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1983: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1984: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1985: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1986: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1987: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1988: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1989: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1990: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1991: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1992: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1993: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1994: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1995: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1996: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      1997: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1998: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      1999: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2000: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2001: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2002: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2003: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2004: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2005: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2006: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2007: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2008: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2009: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2010: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2011: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2012: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2013: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2014: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2015: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2016: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2017: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2018: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2019: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2020: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2021: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2022: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2023: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2024: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2025: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2026: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2027: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2028: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2029: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2030: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2031: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2032: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2033: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2034: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2035: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2036: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2037: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2038: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2039: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2040: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2041: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2042: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2043: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2044: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2045: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2046: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2047: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2048: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2049: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2050: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2051: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2052: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2053: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2054: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2055: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2056: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2057: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2058: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2059: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2060: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2061: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2062: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2063: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2064: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2065: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2066: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2067: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2068: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2069: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2070: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2071: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2072: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2073: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2074: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2075: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2076: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2077: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2078: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2079: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2080: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2081: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2082: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2083: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2084: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2085: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2086: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2087: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2088: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2089: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2090: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2091: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2092: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2093: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2094: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2095: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2096: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2097: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2098: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2099: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2100: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2101: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2102: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2103: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2104: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2105: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2106: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2107: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2108: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2109: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2110: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2111: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2112: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2113: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2114: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2115: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2116: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2117: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2118: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2119: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2120: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2121: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2122: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2123: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2124: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2125: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2126: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2127: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2128: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2129: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2130: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2131: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2132: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2133: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2134: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2135: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2136: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2137: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2138: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2139: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2140: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2141: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2142: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2143: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2144: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2145: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2146: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2147: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2148: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2149: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2150: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2151: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2152: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2153: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2154: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2155: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2156: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2157: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2158: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2159: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2160: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2161: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2162: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2163: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2164: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2165: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2166: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2167: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2168: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2169: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2170: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2171: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2172: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2173: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2174: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2175: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2176: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2177: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2178: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2179: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2180: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2181: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2182: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2183: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2184: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2185: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2186: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2187: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2188: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2189: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2190: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2191: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2192: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2193: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2194: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2195: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2196: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2197: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2198: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2199: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2200: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2201: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2202: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2203: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2204: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2205: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2206: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2207: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2208: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2209: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2210: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2211: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2212: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2213: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2214: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2215: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2216: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2217: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2218: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2219: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2220: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2221: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2222: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2223: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2224: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2225: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2226: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2227: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2228: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2229: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2230: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2231: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2232: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2233: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2234: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2235: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2236: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2237: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2238: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2239: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2240: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2241: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2242: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2243: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2244: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2245: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2246: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2247: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2248: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2249: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2250: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2251: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2252: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2253: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2254: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2255: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2256: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2257: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2258: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2259: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2260: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2261: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2262: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2263: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2264: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2265: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2266: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2267: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2268: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2269: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2270: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2271: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2272: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2273: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2274: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2275: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2276: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2277: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2278: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2279: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2280: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2281: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2282: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2283: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2284: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2285: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2286: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2287: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2288: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2289: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2290: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2291: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2292: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2293: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2294: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2295: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2296: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2297: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2298: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2299: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2300: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2301: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2302: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2303: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2304: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2305: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2306: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2307: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2308: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2309: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2310: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2311: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2312: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2313: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2314: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2315: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2316: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2317: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2318: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2319: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2320: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2321: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2322: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2323: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2324: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2325: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2326: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2327: {
        "de": "Spring 2020",
        "en": "",
        "fr": ""
      },
      2328: {
        "de": "Spring 2020",
        "en": "",
        "fr": ""
      },
      2329: {
        "de": "Spring 2020",
        "en": "",
        "fr": ""
      },
      2330: {
        "de": "Female",
        "en": "",
        "fr": ""
      },
      2331: {
        "de": "Female",
        "en": "",
        "fr": ""
      },
      2332: {
        "de": "Costume 2020",
        "en": "",
        "fr": ""
      },
      2333: {
        "de": "Costume 2020",
        "en": "",
        "fr": ""
      },
      2334: {
        "de": "Costume 2020",
        "en": "",
        "fr": ""
      },
      2335: {
        "de": "Galarian",
        "en": "",
        "fr": ""
      },
      2336: {
        "de": "Galarian",
        "en": "",
        "fr": ""
      },
      2337: {
        "de": "Galarian",
        "en": "",
        "fr": ""
      },
      2338: {
        "de": "Galarian",
        "en": "",
        "fr": ""
      },
      2339: {
        "de": "Galarian",
        "en": "",
        "fr": ""
      },
      2340: {
        "de": "Galarian",
        "en": "",
        "fr": ""
      },
      2341: {
        "de": "Galarian",
        "en": "",
        "fr": ""
      },
      2342: {
        "de": "Galarian Standard",
        "en": "",
        "fr": ""
      },
      2343: {
        "de": "Galarian Zen",
        "en": "",
        "fr": ""
      },
      2344: {
        "de": "Galarian",
        "en": "",
        "fr": ""
      },
      2345: {
        "de": "Galarian",
        "en": "",
        "fr": ""
      },
      2501: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2502: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2503: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2504: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2505: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2506: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2510: {
        "de": "",
        "en": "",
        "fr": ""
      },
      2511: {
        "de": "Shadow",
        "en": "",
        "fr": ""
      },
      2512: {
        "de": "Purified",
        "en": "",
        "fr": ""
      },
      2582: {
        "de": "Galarian",
        "en": "",
        "fr": ""
      },
      2583: {
        "de": "Galarian",
        "en": "",
        "fr": ""
      },
      2585: {
        "de": "Costume 2020",
        "en": "",
        "fr": ""
      },
      2586: {
        "de": "Costume 2020",
        "en": "",
        "fr": ""
      }
    }

    if not value in switch:
      return switch[None][language]
    else:
      return switch[value][language]

  def getCostume(self,value,language):
    switch = {
      ### DEFAULT VALUE
      None: {
        "de": "Hut fehlt",
        "en": "",
        "fr": ""
      },
      0: {
        "de": "",
        "en": "",
        "fr": ""
      },
      1: {
        "de": "Xmas Hat",
        "en": "",
        "fr": ""
      },
      2: {
        "de": "Party Pink",
        "en": "",
        "fr": ""
      },
      3: {
        "de": "Ash Cap",
        "en": "",
        "fr": ""
      },
      4: {
        "de": "Witch Hat",
        "en": "",
        "fr": ""
      },
      5: {
        "de": "Summer 2018",
        "en": "",
        "fr": ""
      },
      6: {
        "de": "Fujiwara",
        "en": "",
        "fr": ""
      },
      7: {
        "de": "Flower Wreath",
        "en": "",
        "fr": ""
      },
      8: {
        "de": "Winter 2018/19",
        "en": "",
        "fr": ""
      },
      9: {
        "de": "Detective",
        "en": "",
        "fr": ""
      },
      10: {
        "de": "Straw Hat",
        "en": "",
        "fr": ""
      },
      11: {
        "de": "Party 2020",
        "en": "",
        "fr": ""
      },
      12: {
        "de": "Flower Hat",
        "en": "",
        "fr": ""
      },
      13: {
        "de": "Safari Zone",
        "en": "",
        "fr": ""
      },
      14: {
        "de": "Halloween 2019",
        "en": "",
        "fr": ""
      },
      15: {
        "de": "Summer 2020",
        "en": "",
        "fr": ""
      },
      16: {
        "de": "Fall 2020",
        "en": "",
        "fr": ""
      },
      17: {
        "de": "Winter 2020",
        "en": "",
        "fr": ""
      },
      18: {
        "de": "NFR_Alpha",
        "en": "",
        "fr": ""
      },
      19: {
        "de": "NFR_Beta",
        "en": "",
        "fr": ""
      },
      20: {
        "de": "NFR_Gamma",
        "en": "",
        "fr": ""
      },
      21: {
        "de": "NFR_NoEvolve",
        "en": "",
        "fr": ""
      },
      22: {
        "de": "Glurak",
        "en": "",
        "fr": ""
      },
      23: {
        "de": "Nachtara",
        "en": "",
        "fr": ""
      },
      24: {
        "de": "Rayquaza",
        "en": "",
        "fr": ""
      },
      25: {
        "de": "Lucario",
        "en": "",
        "fr": ""
      },
      26: {
        "de": "Halloween 2020",
        "en": "",
        "fr": ""
      }
    }

    if not value in switch:
      return switch[None][language]
    else:
      return switch[value][language]

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