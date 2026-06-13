
def parimpar(*args):

	for n in args:
		if n % 2 == 0:
			print(f'{n} é par')
		else:
			print(f'{n} é impar')

parimpar(1, 2, 3, 4, 5, 6, 7)
