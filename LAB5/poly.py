#Veronica Pollock

def poly_add2(poly1, poly2): # parameters must be of degree two
	degree2 = poly1[0] + poly2[0]
	degree1 = poly1[1] + poly2[1]
	degree0 = poly1[2] + poly2[2]
	# print(degree2, "x^2 +", degree1, "x +", degree0 )
	addList = [degree2, degree1, degree0]
	return addList

def poly_mult2(poly1, poly2): # parameters must be of degree two
	degree4 = poly1[0] * poly2[0]
	degree3 = (poly1[0] * poly2[1]) + (poly1[1] * poly2[0])
	degree2 = poly1[1] * poly2[1]
	degree1 = (poly1[1] * poly2[2]) + (poly1[2] * poly2[1])
	degree0 = poly1[2] * poly2[2]
	# print(degree4, "x^4 +", degree3, "x^3 +", degree2, "x^2 +", degree1, "x +", degree0)
	multList = [degree4, degree3, degree2, degree1, degree0]
	return multList

# For testing
# a = [2, 6, 9]
# b = [1, 2, 3]
# listAdd = poly_add2(a,b)
# listMult = poly_mult2(a, b)
# print(listAdd)
# print(listMult)