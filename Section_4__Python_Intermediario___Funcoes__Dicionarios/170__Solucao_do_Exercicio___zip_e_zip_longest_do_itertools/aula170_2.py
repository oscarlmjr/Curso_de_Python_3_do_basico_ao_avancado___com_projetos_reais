# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

def zipar(l1, l2):
	
	return list(zip(l1, l2))


lista_zip = zipar(l1,l2)
print(lista_zip)


# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
# l3 = []

# if len(l1) < len(l2):
#	 for n in range(len(l1)):
#		 l3 += [(l1[n], l2[n])]
# else:
#	 for n in range(len(l2)):
#		 l3 += [(l1[n], l2[n])]

# print(l3)

# cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# uf = ['BA', 'SP', 'MG', 'RJ']
#
# def tamanho(x):
#	 def tamanho_b(y):
#		 if x < y:
#			 return cidade
#		 return uf
#	 return tamanho_b
#
# lista = []
# tamanho_cidade = tamanho(len(cidade))
#
# if cidade == tamanho_cidade(len(uf)):
#	 for n in range(len(cidade)):
#		 lista.append((cidade[n], uf[n]))
# else:
#	 for n in range(len(uf)):
#		 lista.append((uf[n], cidade[n]))
#
# print(lista)



# def listas(func, x):
#	 return func(x)

# tamanho_cidade = listas(tamanho, len(cidade))

# print(tamanho_cidade(len(uf)))
# print(tamanho_cidade(len(uf)))
