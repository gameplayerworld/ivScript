#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import module
import clear
import sys

# set the correct gmt timezone
from datetime import datetime
millis = 1288483950000
ts = millis * 1e-3
utc_offset = datetime.fromtimestamp(ts) - datetime.utcfromtimestamp(ts)
offset = str(utc_offset)
gmt = int(offset[0])

####Lade das Configfile
cfg = config.Config()
try:
  cfg.readConfig(sys.argv[1])
except:
  cfg.readConfig("config.ini")

clear = clear.Clear()
clear.clear(cfg.token,cfg.ivchatId,cfg)

modul = module.Module()
if cfg.nuller == "true":
  modul.nuller(cfg,gmt)
else:
	print("Es wurde nichts aktiviert. Pr\U000000fcfe im Configfile das die Attribute 'rocketStops' oder 'lureModule' auf 'true' gesetzt sind")