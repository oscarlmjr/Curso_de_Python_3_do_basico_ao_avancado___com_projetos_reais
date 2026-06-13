# groupby - agrupando valores (itertools)
from itertools import groupby


alunos = ['a', 'a', 'a', 'a', 'b', 'c']
grupos = groupby(sorted(alunos))


for chave, grupo in grupos:
	print(chave)
	print(list(grupo))

print()

alunos = ['a', 'c', 'a', 'b', 'a', 'a']
grupos = groupby(sorted(alunos))


for chave, grupo in grupos:
	print(chave)
	print(list(grupo))
