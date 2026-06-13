variavel = 'valor'

def func():
	print(variavel)
def func2():
	global variavel  # Não é considerada como boa prática de programação
	variavel = 'Outro valor'
	print(variavel)

func()
func2()

print(variavel)
