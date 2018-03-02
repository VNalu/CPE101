# Project 1 
# 
# Name: Veronica Pollock
# Instructor: S. Einakian 
# Section: 1

#import unittest
from funcs import *

def main():
	#The weight of the user
	userKilo = poundsToKG(float(input("How much do you weigh (pounds)? ")))
	#The distance of the professor
	profDistance = float(input("How far away is your professor (meters)? "))
	#The object the user chooses to throw
	userObject = input("Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? ")
	#The weight of the object the user chooses to throw
	objMass = float(getMassObject(userObject))
	#Calculates the velocity of the object with the distance formula
	userVelObject = float(getVelocityObject(profDistance))
	#The velocity of the skater
	velSkate = getVelocitySkater(objMass, userVelObject, userKilo)

	#so it's on a new line
	print()

	if objMass <= 0.1:
		print("Nice throw! You're going to get an F!")
	elif objMass > 0.1 and objMass <= 1.0:
		print("Nice throw! Make sure your professor is OK.")
	elif profDistance < 20.0:
		print("Nice throw! How far away is the hospital?")
	else:
		print("Nice throw! RIP professor.")
	
	print("Velocity of skater: %0.3f"%velSkate, "m/s")
	
	if velSkate < 0.2:
		print("My grandmother skates faster than you!")
	elif velSkate >= 1.0:
		print("Look out for that railing!!!")

main()
