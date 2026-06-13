"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro
da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário,
retorne o número enviado.
"""

print('Teste Fizzbuzz')
while True:
	from random import randint
	enter = input('Tecle "Enter" para continuar: ')
	if enter == '':
		aleatorio = randint(3, 100)
		if aleatorio % 3 == 0 or aleatorio % 5 == 0:
			def fizzbuzz(num):
				if num % 15 == 0:
					return 'Fizzbuzz'
				if num % 3 == 0:
					return 'fizz'
				if num % 5 == 0:
					return 'buzz'
			print(f'{aleatorio} = {fizzbuzz(aleatorio)}')
		else:
			print(f'{aleatorio} não é divisível '
				  f'por 3 ou por 5.')
