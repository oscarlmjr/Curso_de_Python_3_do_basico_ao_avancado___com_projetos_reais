# Yield from

def gen1():
	yield 2


def gen3():
	yield 2


def gen2(gen):
	yield 1
	yield from gen()
	yield 3
	yield 4


g1 = gen2(gen1)
g2 = gen2(gen3)

for numero in g1:
	print(numero)

print()

for numero in g2:
	print(numero)
