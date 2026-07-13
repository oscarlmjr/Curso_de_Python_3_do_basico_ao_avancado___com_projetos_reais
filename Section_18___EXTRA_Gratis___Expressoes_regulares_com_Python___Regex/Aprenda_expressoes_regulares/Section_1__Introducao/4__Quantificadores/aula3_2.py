# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# * -> 0 ou n
# + -> 1 ou n {1,}
# ? -> 0 ou 1
# {n} -> um número específico
# {min, max}
# {10,} 10 ou mais
# {,10} Especificamente 10
# {5,10} de 5 a 10
# ()+ [a-zA-Z0-9]+
import re


texto2 = 'João ama ser amado'

print(re.findall(r'ama', texto2, flags=re.I))
print(re.findall(r'ama[do]', texto2, flags=re.I))
print(re.findall(r'ama[do]{2}', texto2, flags=re.I))
print(re.findall(r'ama[od]{2}', texto2, flags=re.I))
print(re.findall(r'ama[od]{0,2}', texto2, flags=re.I))
