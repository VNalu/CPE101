# Lab 4
#
# Name: Veronica Pollock
# Instructor: Sussan Einakian
# Section: 23

import driver

def letter(row, col):
	if 3 < row < 6 and 6 < col < 10:
		return "X"
	elif 1 < row < 6 and 3 < col < 10:
		return "Z"
	elif 3 < row < 7 and 6 < col < 13:
		return "B"
	else:
		return "T"

if __name__ == '__main__':
	driver.comparePatterns(letter)
