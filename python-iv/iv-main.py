#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import module
import clear
import sys

####Lade das Configfile
cfg = config.Config()
try:
  cfg.readConfig(sys.argv[1])
except:
  cfg.readConfig("iv-config.ini")

clear = clear.Clear()
clear.clear(cfg.token,cfg.ivchatId,cfg)

modul = module.Module()
if cfg.nuller == "true":
  modul.nuller(cfg)
else:
	print("Es wurde nichts aktiviert. Pr\U000000fcfe im Configfile das die Attribute 'rocketStops' oder 'lureModule' auf 'true' gesetzt sind")