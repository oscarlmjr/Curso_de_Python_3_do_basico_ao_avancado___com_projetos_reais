"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante	'
print(frase.split(' '))
frase = 'Olha só que, coisa interessante'
print(frase.split(' '))
frase = '   Olha só que   , coisa interessante	'
print(frase.split())
print('')

frase = 'Olha só que, coisa interessante '
lista_frases = frase.split(',')
print(lista_frases)
print(frase.split(', '))
print('')

for i, frase in enumerate(lista_frases):
	print(lista_frases[i])
	print(lista_frases[i].strip())
	print(lista_frases[i].rstrip())
	print(lista_frases[i].lstrip())

print(lista_frases)
