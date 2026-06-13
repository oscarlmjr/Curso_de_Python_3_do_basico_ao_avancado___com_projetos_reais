'''
Closure e funções que retornam outras funções
'''

def criar_saudacao(saudacao, nome):
	def saudar():
		return f'{saudacao}, {nome}!'
	return saudar()

print(criar_saudacao('Bom dia', 'Luiz'))
print(criar_saudacao('Boa noite', 'Luiz'), '\n')


def criar_saudacao(saudacao, nome):
	def saudar():
		return f'{saudacao}, {nome}!'
	return saudar

s1 = criar_saudacao('Bom dia', 'Luiz')
s2 = criar_saudacao('Boa noite', 'Luiz')

print(s1())
print(s2())
