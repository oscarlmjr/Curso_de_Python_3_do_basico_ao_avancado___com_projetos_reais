# map - para mapear dados

def printer_iter(iterator):
	print(*iterator, sep='\n')
	print()


produtos = [
	{'nome': 'Produto 5', 'preco': 10.00},
	{'nome': 'Produto 1', 'preco': 22.32},
	{'nome': 'Produto 3', 'preco': 10.11},
	{'nome': 'Produto 2', 'preco': 105.87},
	{'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [{**p, 'preco': 123} for p in produtos]

printer_iter(produtos)
printer_iter(novos_produtos)
