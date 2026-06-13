
lista = [
	{'nome': 'Luiz', 'sobrenome': 'miranda'},
	{'nome': 'Maria', 'sobrenome': 'Oliveira'},
	{'nome': 'Daniel', 'sobrenome': 'Silva'},
	{'nome': 'Eduardo', 'sobrenome': 'Moreira'},
	{'nome': 'Aline', 'sobrenome': 'Souza'},
]

def ordena(item):
	return item['nome']


lista.sort(key=ordena)   # key= só aceita função como argumento

print(lista)

print('')

def ordena(item):
	return item['sobrenome']


lista.sort(key=ordena)

print(lista)

print('')

for item in lista:
	print(item['nome'])
