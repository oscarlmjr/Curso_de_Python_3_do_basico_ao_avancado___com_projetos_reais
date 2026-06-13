# https://www.youtube.com/watch?v=XmCrArtfjaQ
import json


# aspas duplas "" no item
# objecto = {}
# array = []
# number = int ou float
# True = true
# null = None

with open('aula190.json', 'r', encoding='utf8') as arquivo:
	pessoa = json.load(arquivo)
	print(pessoa, '\n')
	print(type(pessoa), '\n')
	print(pessoa['nome'])
