# Lab 3
# 
# Name: Veronica Pollock
# Instructor: S. Einakian 
# Section: 1

# the max of two numbers
def max_101(x, y):
	if x > y:
		return x
	elif y > x:
		return y
	else:
		# because there was no specifications for when they're equal
		print("Holy crackers- they're the saaaaame!")

# the max of three numbers
def max_of_three(x, y, z):
	x = float(x)
	y = float(y)
	z = float(z)
	num = x
	if num < y:
		num = y
	if num < z:
		num = z
	return num

# returns the fee depending on how late the rental was returned
def rental_late_fee(daysLate):
	daysLate = int(daysLate)
	if daysLate <= 0:
		return 0
	elif daysLate <= 9:
		return 5
	elif daysLate <= 15:
		return 7
	elif daysLate <= 24:
		return 19
	else:
		return 100