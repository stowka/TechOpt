#!/usr/python
#-*- coding: utf-8 -*-


from Field import *
from Sensor import *
from Target import *
from Program import *

print "PROJET DE TECHNIQUE D'OPTIMISATION"
print "\tAntoine De Gieter"
print "\tAlexis Beaujon"

field = Field()
choice = 0

while choice != 1 and choice != 2:
	choice = input("1] Configuration aléatoire\n2] Configuration manuelle\n")
	if choice == 1:
		field.initRandom()
		Program.generateLP(field, "problem.lp")
		Program.solve("problem.lp", "solution.sol")
		print "\n"
		Program.interpretation("solution.sol")
	elif choice == 2:
		targets_nb = input("Number of targets:")
		print "---"
		sensors_nb = input("Number of sensors:")
		print "---"
		field.init(targets_nb, sensors_nb)
		Program.generateLP(field, "problem.lp")
		Program.solve("problem.lp", "solution.sol")
		print "\n"
		Program.interpretation("solution.sol")

print "\n---"
print "Merci d'avoir utilisé notre programme, vous pouvez envoyer de l'argent sur le compte bancaire correspondant à l'IBAN suivant :"
print "FR7610278086000002087090196"