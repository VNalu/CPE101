# Project 1 funcs file
# 
# Name: Veronica Pollock
# Instructor: S. Einakian 
# Section: 1

from math import sqrt

def getVelocityObject(distance):
	return(sqrt(9.8*distance/2))

def getVelocitySkater(massObject, velObject, massSkater):
	return((massObject*velObject)/massSkater)

def poundsToKG(pounds):
	return(pounds * 0.453592)

def getMassObject(object):
	if object == "t":
		return 0.1
	elif object == "p":
		return 1.0
	elif object == "r":
		return 3.0
	elif object == "g":
		return 5.3
	elif object == "l":
		return 9.07
	else:
		return 0.0

