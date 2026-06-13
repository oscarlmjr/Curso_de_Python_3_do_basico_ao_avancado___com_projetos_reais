lista = [[x for y in range(3)] for x in range(4)]

print(lista, '\n')

lista = [[y for y in range(3)] for x in range(4)]

print(lista, '\n')

lista = [[letra for letra in 'Luiz'] for x in range(3)]

print(lista, '\n')

lista = [[(x, letra) for letra in 'Luiz'] for x in range(3)]

print(lista, '\n')

lista = [[(x, letra) for x in range(3)] for letra in 'Luiz']

print(lista, '\n')
