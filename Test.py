#!/usr/python
#-*- coding: utf-8 -*-

from Sensor import *
from Target import *

sensor = Sensor()
sensor.initRandom()
print sensor

target = Target()
target.init()
print target
target.initRandom()
print target