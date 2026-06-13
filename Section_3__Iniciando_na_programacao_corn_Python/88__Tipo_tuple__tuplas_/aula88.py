"""
Tipo tupla - Uma lista imutável
"""
nomes = ('Maria', 'Helena', 'Luiz')
nomes = tuple(nomes)
print(nomes, type(nomes))
# nomes[-1] = 'Joana'   # TypeError: 'tuple' object does not support item assignment
print(nomes[-1], '\n')

nomes = 'Maria', 'Helena', 'Luiz'
print(nomes, type(nomes))
print(nomes[-1], '\n')

nomes = list(nomes)
print(nomes, type(nomes))
print(nomes[-1], '\n')
