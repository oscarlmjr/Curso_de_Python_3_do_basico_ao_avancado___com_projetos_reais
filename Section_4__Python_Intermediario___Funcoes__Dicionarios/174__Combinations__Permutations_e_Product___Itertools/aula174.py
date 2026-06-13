# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations


def print_iter(iterator):
	print(*list(iterator), sep='\n')
	print()


pessoas = ['João', 'Joana', 'Luiz', 'Letícia']
camisetas = ['preta', 'branca']


print_iter(combinations(pessoas, 2))
print_iter(combinations(camisetas, 2))
