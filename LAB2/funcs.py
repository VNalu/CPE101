from math import sqrt

def math_func1(x, y):
	result1 = (x*x + y*y) / 3*x + 5
	print("Function 1: ", result1)
	return result1

def math_func2(a, b, c):
	result2 = (-b + sqrt(b*b-4*a*c))/(2*a)
	print("Function 2: ", result2)
	return result2

def math_d(x1, y1, x2, y2):
	result3 = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
	print("Function 3: ", result3)
	return result3

def is_negative(num):
	result = num < 0
	print("Is ", num, "negative?: ", result)
	return result