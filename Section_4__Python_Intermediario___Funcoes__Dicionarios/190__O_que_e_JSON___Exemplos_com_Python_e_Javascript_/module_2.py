# https://www.youtube.com/watch?v=XmCrArtfjaQ
import json
# https://www.youtube.com/watch?v=XmCrArtfjaQ
import os


pessoas = [{"nome": "Luiz Otávio 2", "sobrenome": "Miranda",
  "enderecos": [{"rua": "R1", "numero": 32},
  {"rua": "R2", "numero": 55}],
  "altura": 1.8, "numeros_preferidos": [2, 4, 6, 8, 10],
  "dev": True, "nada": None}]

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'arquivo-python.json')

with open(JSON_FILE, 'r') as file:
  pessoas = json.load(file)
  print(json.dumps(pessoas))
  # print(pessoas)

  # for pessoa in pessoas:
  #   print(pessoa['nome'])
