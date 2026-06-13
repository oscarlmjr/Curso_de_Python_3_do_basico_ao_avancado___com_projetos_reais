# 1 - Crie uma função que exibe uma saudação com os
# parâmetros saudacao e nome.

def saudacao(saudacao, nome):
	nome = input('Digite seu nome: ')
	print(saudacao, nome)

saudacao('Olá', '')

def func(saudacao, nome):
	print(saudacao, nome)

nome = input('Digite seu nome: ')
func('Olá,', nome)
