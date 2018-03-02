# Veronica Pollock

# character as a String -> Boolean
# checks if a character is lowercase
def is_lower_101(char):
	if ord("a") <= ord(char) <= ord("z"):
		return True
	else:
		return False

 
# takes a character and returns the character 13 after it in the alphabet
def char_rot_13(char):
	if 64 < ord(char) < 78:
		rot_13 = ord(char) + 13
		return chr(rot_13)
	elif 77 < ord(char) < 91:
		rot_13 = ord(char) - 13
		return chr(rot_13)
	elif 96 < ord(char) < 110:
		rot_13 = ord(char) + 13
		return chr(rot_13)
	elif 109 < ord(char) < 123:
		rot_13 = ord(char) - 13
		return chr(rot_13)
