
def soma(*args):

	total = 0
	for n in range(len(args)):
		total += args[n]
	return total


soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)

outra_soma = soma(1, 2, 3, 4, 5, 6, 7, 78, 10)
print(outra_soma)

print(sum((1, 2, 3, 4, 5, 6, 7, 78, 10)))
# print(sum(1, 2, 3, 4, 5, 6, 7, 78, 10))   # TypeError: sum() takes at most 2 arguments (9 given)
