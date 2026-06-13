def multi(*args):

	total = 1
	for n in range(len(args)):
		total *= args[n]

	return total

var = multi(1, 2, 3, 4, 5, 6, 7)
print(var)
