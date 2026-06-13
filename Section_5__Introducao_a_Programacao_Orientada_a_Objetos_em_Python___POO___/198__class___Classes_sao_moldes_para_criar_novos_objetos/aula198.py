# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de classes.
# CriarBaseDeDados

# atributos = dados dentro da classe
# métodos = funções dentro da classe

string = 'Luiz'  # str = classe (padrão em Python)
print(string.upper())   # .upper() = método
print(isinstance(string, str))   # string = instância e objeto de str
print(isinstance('Luiz', str))   # 'Luiz' = instância e objeto de str
