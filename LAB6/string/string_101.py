# LAB6
# 
# Name: Veronica Pollock
# Instructor: S. Einakian 
# Section: 1

# string -> string
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

# string -> string
# Takes a string and shifts every letter 13 forward in the alphabet
def str_rot_13(stringInput):
	newString = list(map(lambda x: char_rot_13(x), stringInput))
	return("".join(newString))

# string, string, string -> string
# takes a string and replaces every designated character with a different designated character
def str_translate_101(stringInput, char1, char2):
	listInput = list(stringInput)
	charIndex = 0
	while charIndex < len(listInput): #explicit loop, need implicit
		if listInput[charIndex] == char1:
			listInput[charIndex] = char2
		charIndex += 1
	return "".join(listInput)
