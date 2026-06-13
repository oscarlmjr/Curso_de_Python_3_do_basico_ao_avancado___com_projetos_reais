# groupby - agrupando valores (itertools)
from itertools import groupby


alunos = ['a', 'b', 'c']

grupos = groupby(alunos)

print(grupos, '\n')


for grupo in grupos:
	print(grupo)
