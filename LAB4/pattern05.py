# Lab 4
#
# Name: Veronica Pollock
# Instructor: Sussan Einakian
# Section: 23

import driver

def letter(row, col):
	if col - row >= 0:
		return "W"
	else:
		return "T"

if __name__ == '__main__':
	driver.comparePatterns(letter)
