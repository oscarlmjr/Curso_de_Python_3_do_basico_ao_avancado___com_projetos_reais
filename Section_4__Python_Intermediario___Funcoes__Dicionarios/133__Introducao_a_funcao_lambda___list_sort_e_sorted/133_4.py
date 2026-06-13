lista = [
	{'nome': 'Luiz', 'sobrenome': 'miranda'},
	{'nome': 'Maria', 'sobrenome': 'Oliveira'},
	{'nome': 'daniel', 'sobrenome': 'Silva'},
	{'nome': 'Eduardo', 'sobrenome': 'Moreira'},
	{'nome': 'Aline', 'sobrenome': 'Souza'},
]  # value que começa com letra minúscula vai para o fim da ordem alfabética

def exibir(lista):
	return f'{lista}\n'
	# for item in lista:
	#	 print(item)

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

print(exibir(l1))
print(exibir(l2))

print(lista)
