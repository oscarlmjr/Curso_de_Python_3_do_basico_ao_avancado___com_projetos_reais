# reduce - faz a redução de um iterável em um valor


produtos = [
	{'nome': 'Produto 5', 'preco': 10.00},
	{'nome': 'Produto 1', 'preco': 22.32},
	{'nome': 'Produto 3', 'preco': 10.11},
	{'nome': 'Produto 2', 'preco': 105.87},
	{'nome': 'Produto 4', 'preco': 69.90},
]

total = 0
for p in produtos:
	total += p['preco']


print(round(total, 2))

print()

print(round(sum([p['preco'] for p in produtos]), 2))
