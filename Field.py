#!/usr/python
#-*- coding: utf-8 -*-

import random as rdm
from math import sqrt
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

		for i in range(sensor_nb):
			self._sensors.append(Sensor())
			self._sensors[i].initRandom(self._width)

	def initRandom(self):
		self._width = rdm.randint(5, 10)
		del self._targets[:]
		del self._sensors[:]
		for i in range(rdm.randint(5, 10)):
			self._targets.append(Target())
			self._targets[i].initRandom(self._width)

		for t in self._targets:
			print t
			s = Sensor()
			s.initRandom(self._width)
			while self.sensorCoversTarget(s, t) == False:
				print s
				s = Sensor()
				s.initRandom(self._width)
			self._sensors.append(s)

		# for i in range(rdm.randint(5, 10)):
		# 	self._sensors.append(Sensor())
		# 	self._sensors[i].initRandom(self._width)

	def distanceSensorTarget(self, sensor, target):
		sensor_x = sensor._get_x()
		sensor_y = sensor._get_y()

		target_x = target._get_x()
		target_y = target._get_y()

		return sqrt(pow((sensor_x - target_x), 2) + pow((sensor_y - target_y), 2))

	def sensorCoversTarget(self, sensor, target):
		return sensor._get_radius() >= self.distanceSensorTarget(sensor, target)

	def targetsCoveredBySensor(self, sensor):
		targets = []
		n = 0
		for t in self._targets:
			n += 1
			if self.sensorCoversTarget(sensor, t):
				targets.append(n)
		return targets

	"""
	Getters
	"""
	def _get_width(self):
		return self._width

	def _get_targets(self):
		return self._targets

	def _get_sensors(self):
		return self._sensors