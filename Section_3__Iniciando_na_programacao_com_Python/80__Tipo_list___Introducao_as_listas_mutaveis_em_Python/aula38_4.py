"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend
min, max
range
"""
l2 = [0, 1, 2, 3, 4, 5]
soma = 0
for valor in l2:
	soma = soma + valor
	print(soma)
print('')
l2 = ['String', True, 10, -20.5]
n = 0
for elem in l2:
	print(f'elem: {l2[n]}, tipo {type(elem)} \n'
		  f'e seu valor é {elem}')
	n += 1
