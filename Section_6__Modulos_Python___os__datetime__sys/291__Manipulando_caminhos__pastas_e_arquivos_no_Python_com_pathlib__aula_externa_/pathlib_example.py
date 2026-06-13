"""https://www.youtube.com/watch?v=T17BTNKBeJY"""
from pathlib import Path


caminho_projeto = Path()
print(caminho_projeto.absolute(), '\n')

caminho_arquivo = Path(__file__)
print(caminho_arquivo, '\n')

print(caminho_arquivo.parent, '\n')
print(caminho_arquivo.parent.parent, '\n')
# print(caminho_arquivo.parent.parent.parent, '\n')

ideias = caminho_arquivo.parent / 'ideias'
print(ideias, '\n')
print(ideias / 'arquivo.txt', '\n')

print(Path.home())
print(Path.home() / 'Desktop', '\n')
