
def criar_funcao(func):
	def interna(*args):
		print('Vou te decorar')
		print(*args, args)
		for arg in args:
			print(arg, type(arg))
			e_string(arg)
		resultado = func(*args)
		print(f'O seu resultado foi {resultado}')
		print('Ok, agora você foi decorada.')
		return resultado

	return interna


def inverte_string(string):
	return string[::-1]  # string[-1::-1]

def e_string(param):
	if not isinstance(param, str):
		raise TypeError('param deve ser uma string')


inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)
# print(inverte_string_checando_parametro('123'))
