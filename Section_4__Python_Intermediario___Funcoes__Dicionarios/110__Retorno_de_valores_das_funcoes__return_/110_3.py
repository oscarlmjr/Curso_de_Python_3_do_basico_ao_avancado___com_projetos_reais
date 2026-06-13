'''
Retorno de valores de funções (return)
'''

def soma(x, y):
	return x + y


soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1 + soma2)

print()


def soma(x, y):
	print(x + y)


soma1 = soma(2, 2)
soma2 = soma(3, 3)
# print(soma1 + soma2)   # TypeError: unsupported operand type(s)
						# for +: 'NoneType' and 'NoneType'
