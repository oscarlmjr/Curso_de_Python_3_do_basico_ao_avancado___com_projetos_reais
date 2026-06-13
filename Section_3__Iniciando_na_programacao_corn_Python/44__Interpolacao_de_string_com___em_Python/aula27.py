usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)  # Não funciona com tipos numéricos
print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
	print('Você precisa digitar pelo menos 6 carateres.')
else:
	print('Você foi cadastrado no sistema.')
