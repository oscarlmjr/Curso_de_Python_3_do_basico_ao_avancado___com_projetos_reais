"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
	resultado é 0
contrário disso:
	resultado é o valor da conta
O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)

while True:
	
	digitos = input('Digite um CPF válido: ')
	b = ''

	for n in digitos:
		if n.isdigit():
			b += n

	if b == b[0] * len(b):
		continue

	digitos = b

	soma = 0
	c = 10

	for n in digitos:
		soma += int(n) * c
		c -= 1
		if c == 1:
			break

	resultado = 0
	soma = soma * 10
	resultado = soma % 11

	if resultado > 9:
		resultado = 0

	soma = 0
	c = 11

	for n in digitos:
		soma += int(n) * c
		c -= 1
		if c == 1:
			break

	resultado2 = 0
	soma = soma * 10
	resultado2 = soma % 11

	if resultado2 > 9:
		resultado2 = 0

	if str(resultado) + str(resultado2) == digitos[9] + digitos[10]:
		print('CPF válido.')
	else:
		print('CPF inválido.')
