lista = [
	['P1', 13],
	['P2', 6],
	['P3', 7],
	['P4', 50],
	['P5', 8],
]

def func(item):
	return item[1]

lista.sort(key=func)
print(lista)

lista.sort(key=func, reverse=True)
print(lista)
