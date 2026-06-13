"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante	'
lista_frases = frase.split(',')
print(lista_frases, '\n')


for i, frase in enumerate(lista_frases):
	lista_frases[i] = lista_frases[i].strip()

print(lista_frases, '\n')


frase = '   Olha só que   , coisa interessante	'
lista_frases = frase.split(',')

lista_frase = []
for i, f in enumerate(lista_frases):
	lista_frase.append(lista_frases[i].strip())

print(lista_frase, '\n')

string_unida = '-'.join('abc')
print(string_unida, '\n')

frases_unidas = ', '.join(lista_frase)
print(frases_unidas, type(frases_unidas))
