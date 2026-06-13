# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
	# 0		1
	['Maria', 'Helena', ],  # 0
	# 0
	['Elaine', ],  # 1
	# 0	   1	   2
	['Luiz', 'João', 'Eduarda', ],  # 2
]

a, b, c, *_ = lista
print(a, c, '\n')

p, b, *_, ap, u = lista
print(p, u, ap, '\n')

for nome in lista:
	print(nome, end=' ')
print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print('')

print(*lista)
print(*string)
print(*tupla)
print('')

print(*salas, end='\n')
print(*salas, sep='\n')
