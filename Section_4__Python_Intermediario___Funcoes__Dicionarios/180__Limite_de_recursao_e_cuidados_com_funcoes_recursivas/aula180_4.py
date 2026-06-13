import sys


sys.setrecursionlimit(6)


def recursiva(inicio, fim):
	print(inicio, fim)
	# Caso base
	if inicio >= fim:
		return fim
	# Caso recursivo
	# contar até chegar ao final
	inicio += 1
	return recursiva(inicio, fim)

print(recursiva(0, 5))
