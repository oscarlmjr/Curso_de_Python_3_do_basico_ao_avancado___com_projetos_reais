# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.


def inverte_string(string):
	return string[-1::-1]   # [::-1]


inverte = inverte_string('Luiz')

print(inverte)
