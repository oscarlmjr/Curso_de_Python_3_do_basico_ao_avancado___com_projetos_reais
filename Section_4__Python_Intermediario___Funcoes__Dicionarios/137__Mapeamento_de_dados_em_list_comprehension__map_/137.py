# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# Mapeamento de dados em list comprehension

produtos = [
	{'nome': 'p1', 'preco': 20, },
	{'nome': 'p2', 'preco': 10, },
	{'nome': 'p3', 'preco': 30, },
]


novos_produtos = [produto for produto in produtos]

print(novos_produtos, '\n')
print(*novos_produtos, sep='\n')
