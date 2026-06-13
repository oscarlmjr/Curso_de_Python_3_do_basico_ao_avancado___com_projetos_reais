# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0):
	return 1

gen = generator(n=0)
print(gen, '\n')


def generator(n=0):
	yield 1  # pausar
	return 'ACABOU'

gen = generator(n=0)
print(gen.__iter__())
print(gen.__iter__)
print(next(gen), '\n')
# # print(next(gen))   # StopIteration: ACABOU


def generator(n=0):
	yield 1  # pausar
	print('Continuando...')
	yield 2  # pausar

gen = generator(n=0)
print(next(gen))
print(next(gen), '\n')
print(next(gen))   # StopIteration
