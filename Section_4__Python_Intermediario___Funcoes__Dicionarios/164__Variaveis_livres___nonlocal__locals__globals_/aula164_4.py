# Variáveis livres + nonlocal (locals, globals)
# print(globals())

def concatenar(string_inicial):
	valor_final = string_inicial

	def interna(valor_a_concatenar):
		return valor_final

	return interna

c = concatenar('a')

print(c('b'))
print(c('c'))
print(c('d'))
