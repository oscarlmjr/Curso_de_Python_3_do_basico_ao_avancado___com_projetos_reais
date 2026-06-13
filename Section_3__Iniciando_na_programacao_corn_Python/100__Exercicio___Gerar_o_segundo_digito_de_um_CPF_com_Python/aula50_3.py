cpf = input('Digite (apenas os números) do CPF: ')
if cpf[0].ljust(len(cpf), cpf[0]) == cpf:
	print('CPF inválido')

verificacao = ''
for n in cpf:
	if n == cpf[0]:
		verificacao += n
		if verificacao == cpf:
			print('CPF inválido.')
