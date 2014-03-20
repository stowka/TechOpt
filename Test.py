#!/usr/python
#-*- coding: utf-8 -*-

from Field import *
from Sensor import *
from Target import *
import os

field = Field()
field.init(5, 6)


#
# Generate first line
#
output = "Maximize "
n = 0
for s in field._get_sensors():
	n += 1
	if n > 1:
		output += " + "
	output += "x" + str(n)

output += "\n\nSubject To\n\n"

#
# Generate sensor equations
#
for s in field._get_sensors():
	n = 0
	first = True

	for t in field.targetsCoveredBySensor(s):
		n += 1
		output += "x" + str(t)
		output += " + "
		first = False

	if first == False:
		output = output[:-3]
		output += " <= " + str(s._get_life())
		output += "\n"

output += "\nEND"

with open('qwertz.lp', 'w+') as sol:
	sol.write(output)

os.system("glpsol -o qwertz.sol --cpxlp qwertz.lp --nopresol")


#
#  Generate other lines
#
# for s in field._get_sensors():
# 	for t in field._get_targets():
# 		if 
# 			output += str(t._get_)
# 	output += "\n"
# print output


# print field._get_targets()
# for i in field._get_sensors():
# 	for j in field._get_targets():
# 		print field.sensorCoversTarget(i, j);