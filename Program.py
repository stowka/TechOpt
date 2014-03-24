#!/usr/python
#-*- coding: utf-8 -*-

import os

"""
@project Technique d'optimisation
@author Antoine De Gieter
@author Alexis Beaujon
"""
class Program:
	@staticmethod
	def generateLP(field, name):
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

		with open(str(name), 'w+') as sol:
			sol.write(output)

	@staticmethod
	def solve(input, output):
		os.system("glpsol -o " + str(output) + " --cpxlp " + str(input) + " --nopresol")

	@staticmethod
	def interpretation(file):
		content = []
		i = 0
		with open(file, "r") as sol:
			for line in sol:
				content = line.split()
				if content:
					if content[0] == "Status:":
						print "Pour avoir une solution de type " + str(content[1]) + " il faut que :"
					if content[0] == "No." and content[1] == "Column":
						i = 1
					if content[0] == str(i):
						if content[3] != str(0):
							print "- le Sensor " + str(i) + " soit actif pendant " + str(content[3]) + "h"
						i += 1
