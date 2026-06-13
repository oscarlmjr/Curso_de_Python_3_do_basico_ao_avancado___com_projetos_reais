# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def criar_funcao(func):
	print(func.__name__, type(func))
	def interna(*args):
		print('Vou te decorar')
		print(*args, args)
		for arg in args:
			print(arg)
			e_string(arg)
		print(f'func(*args) = {func(*args)}')
		resultado = func(*args)
		print(f'O seu resultado foi {resultado}.')
		print('Ok, agora você foi decorada')
		return resultado
	return interna

@criar_funcao
def inverte_string(string):
	print(f'inverte_string.__name__ = {inverte_string.__name__}')
	return string[::-1]

def e_string(param):
	if not isinstance(param, str):
		raise TypeError('param deve ser uma string')


invertida = inverte_string('123')
print(invertida)
