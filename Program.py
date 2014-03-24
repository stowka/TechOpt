#!/usr/python
#-*- coding: utf-8 -*-

from Field import *
from Sensor import *
from Target import *
import os

"""
@project Technique d'optimisation
@author Antoine De Gieter
@author Alexis Beaujon
"""
class Program:
	__shared_state = {}
	def __init__(self):
		self.__dict__ = self.__shared_state

	def generateLP(self, name):
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

		with open(str(name) + '.lp', 'w+') as sol:
			sol.write(output)

	def solve(self, input, output):
		os.system("glpsol -o " + str(output) + " --cpxlp " + str(input) + " --nopresol")
		