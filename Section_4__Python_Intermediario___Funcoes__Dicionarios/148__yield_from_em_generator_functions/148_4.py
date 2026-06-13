# Yield from

def gen1():
	yield 2


def gen3():
	yield 2


def gen2(gen=None):
	yield 1
	if gen is not None: yield from gen
	else: yield 2; yield 3
	yield 4
	print()


g1 = gen2(gen1());  g2 = gen2(gen3()); g3 = gen2()

for numero in g1:
	print(numero)

for numero in g2:
	print(numero)

for numero in g3:
	print(numero)
