
def mostro_argumentos_nomeados(*args, **kwargs):
	print('Não nomeados: ', args, '\n')

	for chave, valor in kwargs.items():
		print(chave, valor)

	print()

mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)
