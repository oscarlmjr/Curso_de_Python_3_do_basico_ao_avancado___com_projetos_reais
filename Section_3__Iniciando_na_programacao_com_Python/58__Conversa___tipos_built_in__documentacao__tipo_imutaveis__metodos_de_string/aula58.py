"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'Luiz Otávio'
outra_variavel = string

print(string)
print(string[3])
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(outra_variavel)
print(string.capitalize())


string = '1000'
print(string)
print(string.zfill(10))
