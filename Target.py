#!/usr/python
#-*- coding : utf-8 -*-
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
		self._x = x
		self._y = y

	def __str__(self):
		return "[" + self._x + ", " + self._y + "]"

	def _get_x(self):
		return self._x

	def _get_y(self):
		return self._y

