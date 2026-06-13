# 2 - Crie uma função que receba 3 números como parâmetros e
# exiba a soma entre eles.

def soma(n1, n2, n3):
	print(n1 + n2 + n3)
soma(1, 2, 3)

def soma(num_1, num_2, num_3):
	return num_1 + num_2 + num_3
for n in range(3):
	num = int(input('Digite um número: '))
	if n == 0:
		n_1 = num
	elif n == 1:
		n_2 = num
	else:
		n_3 = num

print(soma(num_1=n_1, num_2=n_2, num_3=n_3))
