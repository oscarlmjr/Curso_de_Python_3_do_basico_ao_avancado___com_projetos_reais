
configuracoes = {'arg1': 1, 'arg2': 2, 'arg3': 3, 'arg4': 4,}


print(*configuracoes, '\n')


def mostro_argumentos_nomeados(*args, **kwargs):
	print('Não nomeados: ', args, '\n')

	for chave, valor in kwargs.items():
		print(chave, valor)


mostro_argumentos_nomeados(**configuracoes)
