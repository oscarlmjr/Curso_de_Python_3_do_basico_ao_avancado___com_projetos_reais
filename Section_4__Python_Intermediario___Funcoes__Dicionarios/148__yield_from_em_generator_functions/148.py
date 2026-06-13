# Yield from

def gen1():
	return 'gen1'

g = gen1()


for numero in g:   # for numero in gen2():
	print(numero)

print()


def gen1():
	yield 1
	yield 2
	yield 3

def gen2():
	yield from gen1()
	yield 4
	yield 5
	yield 6

g = gen2()

for numero in g:   # for numero in gen2():
	print(numero)
