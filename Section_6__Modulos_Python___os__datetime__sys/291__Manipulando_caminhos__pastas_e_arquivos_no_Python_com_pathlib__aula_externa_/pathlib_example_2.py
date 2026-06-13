"""https://www.youtube.com/watch?v=T17BTNKBeJY"""
from pathlib import Path


caminho_projeto = Path()
print(caminho_projeto.absolute(), '\n')

caminho_arquivo = Path(__file__)

ideias = caminho_arquivo.parent / 'ideias'

print(Path.home())
print(Path.home() / 'Desktop', '\n')

arquivo = Path.home() / 'Desktop' / 'arquivo.txt'

arquivo.touch()
print(arquivo, '\n')
arquivo.unlink()
