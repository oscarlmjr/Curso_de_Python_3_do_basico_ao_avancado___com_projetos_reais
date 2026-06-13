# isistance - para saber se o objeto é de determindado tipo

lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Luiz'},]

for item in lista:
	if isinstance(item, set):
		item.add(5)
		print('set')
		print(item, isinstance(item, set))

	elif isinstance(item, str):
		print('str')
		print(item.upper(), isinstance(item, set))

	elif isinstance(item, (int, float)):
		print('int or float')  # True isinstance int, True isinstance bool
		print(item, item * 2)

	else:
		print('Outro')
		print(item,)
	print()
