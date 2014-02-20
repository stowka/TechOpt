#!/usr/python
#-*- coding: utf-8 -*-

import random as rdm

"""
@project Technique d'optimisation
@author Antoine De Gieter
@author Alexis Beaujon
"""
class Sensor:
	"""
	Sensor:
		x: position x
		y: position y
		radius: coverage radius
		life: battery
	"""

	def __init__(self):
		self._x = 0
		self._y = 0
		self._radius = 0
		self._life = 0

	def __str__(self):
		return "[SENSOR] Coordinates: [" + str(self._x) + ", " + str(self._y) + ", " + str(self._radius) + "]\nLife: [" + str(self._life) + "]\n"

	def init(self):
		self._x = input("X = ")
		self._y = input("Y = ")
		self._radius = input("Radius = ")
		self._life = input("Life = ")

	def initRandom(self, width):
		self._x = rdm.randint(0, width)
		self._y = rdm.randint(0, width)
		self._radius = rdm.randint(1, 3)
		self._life = rdm.randint(2, 6)

	"""
	Getters
	"""
	def _get_x(self):
		return self._x

	def _get_y(self):
		return self._y

	def _get_radius(self):
		return self._radius

	def _get_life(self):
		return self._life