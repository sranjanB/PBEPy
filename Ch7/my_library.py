# A simple list
my_list = [1, 2, 3, 4]

# A Simple Dictionary

my_dictionary = {1:"Jack", 2:"Kate", 3:"Bob"}

def make_total_double(first, second):
	"""
	This function takes two numbers
	and return double.
	"""
	total = first + second
	return total * 2

def make_average(first, second, third = 0):
	"""
	This function take three numbers and
	returns the average.
	The third is optional.
	"""
	total = first + second + third
	return total / 3
