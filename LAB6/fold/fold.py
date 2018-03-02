# Veronica Pollock

# list -> integer
# takes a list and returns the sum of all the values in the list
def sum(inputList):
	listSum = 0
	for item in inputList:
		listSum += item
	return listSum

# list -> integer
# takes a list and returns the index of the smallest value in the list
def index_of_smallest(inputList):
	if len(inputList) <= 0:
		return -1
	else:
		smallestValueIndex = 0
		for index in range(len(inputList)):
			if inputList[index] < inputList[smallestValueIndex]:
				smallestValueIndex = index

	return smallestValueIndex
