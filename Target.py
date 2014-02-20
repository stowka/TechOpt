#!/usr/python
#-*- coding : utf-8 -*-

import random as rdm

"""
@project Technique d'optimisation
@author Antoine De Gieter
@author	Alexis Beaujon
"""

class Target:
	"""
	Target:
		x : position x
		y : position y
	"""

	def __init__(self):
		self._x = 0
		self._y = 0

	def __str__(self):
		return "[TARGET] Coordinates: [" + str(self._x) + ", " + str(self._y) + "]\n"
		
	def init(self):
		self._x = input("X = ")
		self._y = input("Y = ")
	
	def initRandom(self, width):
		self._x = rdm.randint(0, width)
		self._y = rdm.randint(0, width)
	
	"""
	Getters
	"""

	def _get_x(self):
		return self._x

	def _get_y(self):
		return self._
