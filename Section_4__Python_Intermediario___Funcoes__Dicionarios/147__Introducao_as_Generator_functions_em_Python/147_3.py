# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator():
	yield 1
	print('Continuando...')
	yield 2
	print('Mais uma...')
	yield 3
	print('Vou terminar', '\n')
	return 'Acabou'


gen = generator()

for next in gen:
	print(next, '\n')

print(gen, '\n')
