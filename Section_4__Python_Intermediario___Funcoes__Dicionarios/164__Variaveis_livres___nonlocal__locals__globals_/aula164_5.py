# Variáveis livres + nonlocal (locals, globals)

def concatenar(string_inicial):
	valor_final = string_inicial

	def interna(valor_a_concatenar=''):
		nonlocal valor_final
		# UnboundLocalError: cannot access local variable 'valor_final'
		# where it is not associated with a value
		valor_final += valor_a_concatenar
		return valor_final

	return interna

c = concatenar('a')

print(c())
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)
