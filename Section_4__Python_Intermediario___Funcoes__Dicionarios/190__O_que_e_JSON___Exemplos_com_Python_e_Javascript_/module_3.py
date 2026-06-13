# https://www.youtube.com/watch?v=XmCrArtfjaQ
import json
import os


pessoas = [{"nome": "Luiz Otávio 2", "sobrenome": "Miranda",
  "enderecos": [{"rua": "R1", "numero": 32},
  {"rua": "R2", "numero": 55}],
  "altura": 1.8, "numeros_preferidos": [2, 4, 6, 8, 10],
  "dev": True, "nada": None}]

json_string = '''
[{"nome": "Luiz Ot\u00e1vio 2", "sobrenome": "Miranda",
"enderecos": [{"rua": "R1", "numero": 32}, {"rua": "R2", 
"numero": 55}], "altura": 1.8, 
"numeros_preferidos": [2, 4, 6, 8, 10], "dev": true, "nada": null}]
'''

pessoas = json.loads(json_string)

for pessoa in pessoas:
  print(pessoa['nome'])
