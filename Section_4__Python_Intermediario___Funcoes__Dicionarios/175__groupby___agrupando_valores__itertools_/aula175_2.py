# groupby - agrupando valores (itertools)
from itertools import groupby


alunos = ['a', 'a', 'a', 'a', 'b', 'c']
grupos = groupby(alunos)


for chave, grupo in grupos:
	print(chave)
	print(list(grupo))
print()


alunos = ['a', 'a', 'a', 'a', 'b', 'c', 'a']
grupos = groupby((alunos))


for chave, grupo in grupos:
	print(chave)
	print(list(grupo))
