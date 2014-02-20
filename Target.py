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

	def __init__(self, x, y):
		print "New target\n"
		self._x = 0
		self._y = 0
		print self

	def __str__(self):
		return "[" + self._x + ", " + self._y + "]"
		
	def init(self):
		self._x = input("X:")
		self._y = input("Y:")
	
	def initRandom(self):
		self._x = rdm.random(0,10)
		self._y = rdm.random(0,10)
	
	"""
	Getters
	"""

	def _get_x(self):
		return self._x

	def _get_y(self):
		return self._
