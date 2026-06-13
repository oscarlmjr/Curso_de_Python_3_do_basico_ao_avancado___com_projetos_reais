# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def numero(valor, m_2, m_3, m_4):

	def duplicar():
		return f'{valor} * {m_2} = {valor * m_2}'

	def triplicar():
		return f'{valor} * {m_3} = {valor * m_3}'

	def quadruplicar():
		return f'{valor} * {m_4} = {valor * m_4}'

	return duplicar, triplicar, quadruplicar

var, var_2, var_3 = numero(4, 2, 3, 4)

print(f'{var()}\n{var_2()}\n{var_3()}')


# def multiplicar(x, y):
#	 return x * y
#
# for x in [0, 1, 2, 3, 4]:
#	 for y in range(2, 5):
#		 if y ==2:
#			 duplicar = multiplicar(x, y)
#			 print(f'O dobro de {x} é {duplicar}')
#		 elif y == 3:
#			 triplicar = multiplicar(x, y)
#			 print(f'O triplo de {x} é {triplicar}')
#		 else:
#			 quadruplicar = multiplicar(x, y)
#			 print(f'O quadruplo de {x} é {quadruplicar}', '\n')


# def duplicar(x):
#	 print(f'{x} * 2 = {x * 2}')
#
#	 def triplicar(x):
#		 print(f'{x} * 3 = {x * 3}')
#
#		 def quadruplicar(x):
#			 return f'{x} * 4 = {x * 4}\n'
#
#		 return quadruplicar(x)
#
#	 return triplicar(x)
#
#
# for x in [0, 1, 2, 3, 4]:
#	 print(duplicar(x))


# def multiplicar(muliplicador):
#
#	 def numero_valor(numero):
#		 return numero * muliplicador
#
#	 return numero_valor
#
# n = 2
# valor = multiplicar(2)
# print(valor(n))
# valor = multiplicar(3)
# print(valor(n))
# valor = multiplicar(4)
# print(valor(n))


# def multiplicar(multiplicador):
#
#	 def valor(numero):
#		 return multiplicador * numero
#
#	 return valor
#
#
# duplicar = multiplicar(2)
# triplicar = multiplicar(3)
# quadruplicar = multiplicar(4)
#
# print(duplicar(3))
# print(triplicar(3))
# print(quadruplicar(3))


# def duplica(numero):
#	 print(numero * 2)

#	 def triplica(numero):
#		 print(numero * 3)

#		 def quadruplica(numero):
#			 return numero * 4
		
#		 return quadruplica(numero)
	
#	 return triplica(numero)


# print(duplica(numero=2))
