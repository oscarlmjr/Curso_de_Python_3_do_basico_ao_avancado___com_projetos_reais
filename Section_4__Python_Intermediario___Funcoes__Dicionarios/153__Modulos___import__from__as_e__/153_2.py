# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
from sys import exit, platform


platform = 'A MINHA'

print(platform)


from sys import exit, platform


print(platform)

exit()
print('Não imprime')
