#  continue - pula para o próximo laço
#  break - termina o laço

texto = 'Python'
nova_string = ''
for letra in texto:
	if letra == 't':
		continue
		nova_string += letra.upper()
	elif letra == 'o':
		nova_string += letra.upper()
		break
	else:
		nova_string += letra
print(nova_string)
