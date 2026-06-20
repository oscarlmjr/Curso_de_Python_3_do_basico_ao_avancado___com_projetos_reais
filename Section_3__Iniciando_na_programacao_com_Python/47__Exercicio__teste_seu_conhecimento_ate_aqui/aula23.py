"""
Entrada de dados
"""
nome = input("Qual o seu nome? ")
print(f'{nome} {type(nome)}')
idade = input("Qual a sua idade? ")  # Apenas para Strings
print(f'{idade} {type(idade)}')
ano_nascimento = 2022-int(idade)
print(f'{nome} tem {idade} anos.\n'
	  f'{nome} nasceu em {ano_nascimento}')
print()
