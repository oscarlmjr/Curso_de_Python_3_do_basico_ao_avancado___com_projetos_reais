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

# texto = '''
# <p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
# '''
texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div> 
'''

print(re.findall(r'<[dpiv]{1,3}>.+<\/[dpiv]{1,3}>', texto))
print(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto))
# print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', texto))
# print(re.findall(r'<[dpiv]{1,3}>.?<\/[dpiv]{1,3}>', texto))
# print(re.findall(r'<([dpiv]{1,3})>.*', texto))
