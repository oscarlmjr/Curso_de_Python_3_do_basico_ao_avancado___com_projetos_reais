
pessoa = {'nome': 'Aline', 'sobrenome': 'Souza'}

for chave, valor in pessoa.items():
	print(chave, valor)

print()

dados_pessoa = {'idade': 16, 'altura': 1.6,}

pessoas_completa = {**pessoa, **dados_pessoa, 'chave': 1}
print(pessoas_completa, type(pessoas_completa), '\n')


dados_pessoa = {'idade': 16, 'altura': 1.6,}

pessoas_completa = {*pessoa, *dados_pessoa}
print(pessoas_completa, type(pessoas_completa))
