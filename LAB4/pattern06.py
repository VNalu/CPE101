# Lab 4
#
# Name: Veronica Pollock
# Instructor: Sussan Einakian
# Section: 23

import driver

def letter(row, col):
	if col-row==0 or col+row==6:
		return "X"
	else:
		return "O"

if __name__ == '__main__':
	driver.comparePatterns(letter)
