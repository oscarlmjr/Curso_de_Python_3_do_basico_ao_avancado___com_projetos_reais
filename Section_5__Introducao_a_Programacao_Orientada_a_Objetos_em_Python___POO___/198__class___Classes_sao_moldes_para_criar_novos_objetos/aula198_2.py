# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# CriarBaseDeDados

class Pessoa:
	...

p1 = Pessoa()
p1.nome = 'Luiz'   # .valor após a instância = atributo
p1.sobrenome = 'Otavio'
print(p1)
print(p1.nome)
print(p1.sobrenome)

p2 = Pessoa()
p2.nome = 1
p2.sobrenome = True
print(p2)
print(p2.nome)
print(p2.sobrenome)
