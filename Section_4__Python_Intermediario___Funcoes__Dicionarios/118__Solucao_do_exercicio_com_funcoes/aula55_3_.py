# 3 - Crie uma função que receba 2 números. O primeiro
# é um valor e o segundo um percentual (ex. 10%). Retorne
# (return) o valor do primeiro número somado do aumento
# do percentual do mesmo. Exibir o valor na tela.

def percentual(num_1, num_2):
	return (f'{num_1 * (1 + (num_2/100)):.2f}')
for n in range(2):
	if n == 0:
		num = int(input('Digite um número: '))
		num_1 = num
	if n == 1:
		num = int(input('Digite um valor percentual: '))
		num_2 = num
print(percentual(num_1=num_1, num_2=num_2))


# def porcentagem(n1, n2):
#	 return n2 * n1
# while True:
#	 c = 0
#	 n1 = 0
#	 while c < 2:
#		 numero = int(input('Digite um número: '))
#		 n1, n2 = numero, n1
#		 if c > 0:
#			 n1 = (n1 / 100) + 1
#		 c += 1
#	 print(f'{n2} somado a {numero}% do seu valor é '
#		   f'igual a: {porcentagem(n2, n1):.2f}')


# def porcentagem(n1, n2):
#	 return n1 * n2
#
# print(f'{porcentagem(100, 1.1):.2f}')
# percent = porcentagem(100, 1.1)
# print(f'{percent:.2f}')


# while True:
#	 def porcentagem(n1=0, n2=0):
#		 c = 0
#		 while c < 2:
#			 numero = int(input('Digite um número: '))
#			 n1, n2 = numero, n1
#			 if c > 0:
#				 n1 = (n1 / 100) + 1
#				 print(f'{n2} somado a {numero}% do seu valor é igual a: {(n2 * n1):.2f}')
#			 c += 1
#	 porcentagem()
