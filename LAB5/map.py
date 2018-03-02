
# squareList = [1, 2, 3, 4] # Test
def square_all(list):
	newList = list
	for i in range(len(list)):
		newList[i] = list[i]**2
	return newList
# print(square_all(squareList)) # Test

def add_n_all(list, n):
	newList = list
	i = 0
	while i < len(list):
		newList[i] = list[i] + n
		i += 1
	return newList
# print(add_n_all([1, 2, 3, 4, 5], 100)) # Test

def even_or_odd_all(input_list):
    return [input_list[i] % 2 == 0 for i in range(0,len(input_list))]
# print(even_or_odd_all([1, 2, 3, 4, 5])) # Test
