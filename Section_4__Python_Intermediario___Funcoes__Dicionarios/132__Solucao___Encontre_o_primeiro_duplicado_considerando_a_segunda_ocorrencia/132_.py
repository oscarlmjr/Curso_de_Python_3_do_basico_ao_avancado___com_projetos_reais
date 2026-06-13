lista_de_listas = [
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	[9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
	[1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
	[3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
	[4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
	[1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
	[10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
	[1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
	[1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
	[4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
	[5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
	[10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def funcao(parm):

	
	if len(set(l)) == len(l):
		print(-1)
	else:
		for n in l:
			c = 0
			for p in l: 
				if n == p:
					c += 1
					if c == 2:
						print(n)
						break
			if c == 2:
				break
				
for l in lista_de_listas:
	funcao(l)
		

# def lista(lista_de_listas):
#	 n_set = set()
#	 cont = 0
#	 for n in lista_de_listas:
#		 n_set = set(n)
#		 if len(n_set) == len(n):
#			 var = print(f'lista_de_listas[{cont}] = -1')
#		 else:
#			 c = len(n) - 1
#			 for _ in n:
#				 if n[-c] in n[:-c]:
#					 var = print(f'lista_de_listas[{cont}] = {n[-c]}')
#					 break
#				 c -= 1
#				 if c < 1:
#					 break
#		 cont += 1
#	 return var
# lista(lista_de_listas)


# def elemento_repetido(lista):

#	 if len(lista) == len(set(lista)):
#		 return f'{lista}, -1'
#	 lista_elemento = []
#	 set_elemento = set()

#	 for elemento in lista:
#		 lista_elemento.append(elemento)
#		 set_elemento.add(elemento)
#		 if len(set_elemento) == len(lista_elemento):
#			 continue
#		 else:
#			 return f'{lista}, {elemento}'


# for lista in lista_de_listas:
#	 print(elemento_repetido(lista))
