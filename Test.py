#!/usr/python
#-*- coding: utf-8 -*-

from Field import *
from Sensor import *
from Target import *

field = Field()
field.init(3, 3)
for i in field._get_sensors():
	for j in field._get_targets():
		print i, j;
		print field.sensorCoversTarget(i, j);
		print "\n";