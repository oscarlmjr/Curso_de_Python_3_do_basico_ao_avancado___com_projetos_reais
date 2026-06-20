from random import randint
while True:
	numeros = str(randint(100000000, 999999999))
	enter = input('Tecle \'Enter\' para gerar um CPF: ')
	c = 10
	cont = 0
	soma = 0
	while len(numeros) < 11:
		for n in numeros:
			d = int(n)
			soma += d * c
			c -= 1
		c = 11
		soma = 11 - (soma % 11)
		digito = soma
		soma = 0
		if digito > 9:
			digito = 0
			numeros += str(digito)
		elif digito <= 9:
			numeros += str(digito)
		cont += 1
	print(f'O CPF gerado foi: {numeros}\n')
