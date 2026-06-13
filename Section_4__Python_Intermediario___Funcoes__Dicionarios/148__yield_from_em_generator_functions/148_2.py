# Yield from

def gen1():
	yield 1
	yield 2
	yield 3


def gen2(gen):
	yield from gen()
	yield 4
	yield 5
	yield 6


g = gen2(gen1)

for numero in g:   # for numero in gen2():
	print(numero)
