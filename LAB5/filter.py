def are_positive(list):
	newList = []
	for i in range(len(list)):
		if list[i] > 0:
			newList.append(list[i])
	return newList
# print(are_positive([-2, -1, 0, 1, 2, 3])) # test

def are_greater_than_n(list, n):
	newList = []
	listLength = len(list)
	i = 0
	while i < listLength:
		if list[i] > n:
			newList.append(list[i])
		i += 1
	return newList
# print(are_greater_than_n([1, 2, 3, 4, 5], 3)) # test

# n = 3
# listGreat = [1, 2, 3, 4, 5]
# are_greater_than_n = list(filter(lambda x: x > n, listGreat))
# print(are_greater_than_n)

def listDiv(list, n):
	return [list[i] for i in range(len(list)) if list[i] % n == 0]
# print(listDiv([9, 8, 7, 6, 5, 4, 3, 2], 3)) # test

# n = 2
# listDiv = [1, 2, 3, 4, 5]
# are_divisible_by_n = list(filter(lambda x: x % n == 0, listDiv))
# print(are_divisible_by_n)