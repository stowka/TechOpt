#!/usr/python
#-*- coding: utf-8 -*-

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
		print "New Sensor\n"
		self._x = 0
		self._y = 0
		self._radius = 0
		self._life = 0
		print self

	def __str__(self):
		return "[" + self._x + ", " + self._y + ", " + self._radius + "]"

	def init(self):
		self._x = input("X:")
		self._y = input("Y:")
		self._radius = input("Radius")
		self._life = input("Life:")

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