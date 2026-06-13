
lista = []

for x in range(3):
	for y in range(3):
		lista.append((x, y))

print(lista, '\n')

lista = [(x, y) for x in range(3) for y in range(4)]

print(lista, '\n')
