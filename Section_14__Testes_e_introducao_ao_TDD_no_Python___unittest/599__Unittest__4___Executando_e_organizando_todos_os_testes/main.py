# https://docs.python.org/3/library/doctest.html
# http://docs.python.org/3/library/unittest.html#module-unittest
from calculadora import soma

# print(soma(10, 20))
# print(soma(-10, 20))
# print(soma(-1.5, 2.5))

try:
	print(soma('15', 15))
except AssertionError as e:
	print(f'Conta inválida: {e}')

print('Conta', soma(15, 15))
