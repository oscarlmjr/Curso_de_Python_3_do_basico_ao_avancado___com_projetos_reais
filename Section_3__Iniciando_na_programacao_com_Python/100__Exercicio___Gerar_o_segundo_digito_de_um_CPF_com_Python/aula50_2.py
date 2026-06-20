while True:
	cpf = input('Digite (apenas os números) do CPF: ')
	if cpf == '':
		print('Digite um CPF válido.')
		continue
	if cpf[0].ljust(len(cpf), cpf[0]) == cpf:
		print('Digite um CPF válido.')
	else:
		if cpf.isdigit():
			if len(cpf) == 11:
				cont2 = 9
				while cont2 < 11:
					soma = 0
					cont = 0
					for n in cpf[:cont2:1]:
						digito = int(n)
						soma += digito * ((cont2 + 1) - cont)
						cont += 1
					verificacao = 11 - (soma % 11)
					soma = 0
					cont = 0
					proximo_digito = int(cpf[cont2])
					if verificacao > 9 and proximo_digito == 0 or \
						proximo_digito == 9 or verificacao == proximo_digito:
						valido = True
					else:
						valido = False
						break
					cont2 += 1
				if valido is True:
					print('CPF válido.')
				else:
					print('CPF inválido.')
			else:
				print('Um CPF válido possui onze digitos.')
		else:
			print('Apenas números.')
