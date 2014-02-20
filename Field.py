#!/usr/python
#-*- coding: utf-8 -*-

import random as rdm
from math import sqrt, pow
from Sensor import *
from Target import *

"""
@project Technique d'optimisation
@author Antoine De Gieter
@author Alexis Beaujon
"""
class Field:
	"""
	Field:
		width: square width
	"""

	def __init__(self):
		self._width = 0
		self._targets = []
		self._sensors = []

	def __str__(self):
		return "[FIELD] Width: [" + str(self._width) + "]\n"

	def init(self, target_nb, sensor_nb):
		self._width = input("Width = ")
		del self._targets[:]
		del self._sensors[:]
		for i in range(target_nb):
			self._targets.append(Target())
			self._targets[i].initRandom(self._width)
			print self._targets[i]


		for i in range(sensor_nb):
			self._sensors.append(Sensor())
			self._sensors[i].initRandom(self._width)
			print self._sensors[i]

	def initRandom(self):
		self._width = rdm.randint(5, 100)

	def distanceSensorTarget(self, sensor, target):
		sensor_x = sensor._get_x()
		sensor_y = sensor._get_y()

		target_x = target._get_x()
		target_y = target._get_y()

		return sqrt(pow((sensor_x - target_x), 2) + pow((sensor_y - target_y), 2))

	def sensorCoversTarget(self, sensor, target):
		return sensor._get_radius() >= distanceSensorTarget(sensor, target)

	"""
	Getters
	"""
	def _get_width(self):
		return self._width

	def _get_targets(self):
		return self._targets

	def _get_sensors(self):
		return self._sensors