# LAB6
# 
# Name: Veronica Pollock
# Instructor: S. Einakian 
# Section: 1

# character as a String -> Boolean
# checks if a character is lowercase
def is_lower_101(char):
	if ord("a") <= ord(char) <= ord("z"):
		return True
	else:
		return False

# string -> string
# takes a character and returns the character 13 after it in the alphabet
def char_rot_13(char):
	if ord("B") <= ord(char) <= ord("M"):
		rot_13 = ord(char) + 13
		return chr(rot_13)
	elif ord("O") <= ord(char) <= ord("Z"):
		rot_13 = ord(char) - 13
		return chr(rot_13)
	elif ord("a") <= ord(char) <= ord("m"):
		rot_13 = ord(char) + 13
		return chr(rot_13)
	elif ord("n") <= ord(char) <= ord("z"):
		rot_13 = ord(char) - 13
		return chr(rot_13)
