
produtos = [
	{'nome': 'p1', 'preco': 20, },
	{'nome': 'p2', 'preco': 10, },
	{'nome': 'p3', 'preco': 30, },
]


novos_produtos = [{**produto} for produto in produtos]
# novos_produtos = [produto for produto in produtos]
# novos_produtos = [{produto} for produto in produtos]  # TypeError: unhashable 
# type: 'dict'

print(novos_produtos)

print()

print(*novos_produtos, sep='\n')
