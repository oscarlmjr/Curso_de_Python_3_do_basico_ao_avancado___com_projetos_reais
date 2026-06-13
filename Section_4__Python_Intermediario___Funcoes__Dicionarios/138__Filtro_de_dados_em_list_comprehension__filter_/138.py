# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
import pprint


produtos = [
	{'nome': 'p1', 'preco': 20, },
	{'nome': 'p2', 'preco': 10, },
	{'nome': 'p3', 'preco': 30, },
]


novos_produtos = [
	{**produto, 'preco': produto['preco'] * 1.05}
	if produto['preco'] > 20 else {**produto}
	for produto in produtos
]

pprint.pprint(novos_produtos, sort_dicts=False, width=40)
