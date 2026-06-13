"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 50:
	contador += 1

	if contador >= 10 and contador <= 15:
		print(f'Vou mostrar o {contador}.')
		continue

	if contador >= 10 and contador <= 20:
		print('Não vou mostrar o', contador)
		continue

	print(contador)

	if contador == 25:
		break


print('Acabou')
