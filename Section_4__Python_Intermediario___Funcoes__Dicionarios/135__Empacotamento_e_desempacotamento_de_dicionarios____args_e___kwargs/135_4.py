
pessoa = {'nome': 'Aline', 'sobrenome': 'Souza'}

dados_pessoa = {'idade': 16, 'altura': 1.6,}

pessoas_completa = {**pessoa, **dados_pessoa, 'chave': 1}


def mostro_argumentos_nomeados(*args, **kwargs):
	print(f'Não nomeados: {args}', type(args), '\n')

	for chave, valor in kwargs.items():
		print(chave, valor)


mostro_argumentos_nomeados(**pessoas_completa)
