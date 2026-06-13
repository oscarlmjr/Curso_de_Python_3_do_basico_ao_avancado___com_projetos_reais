"""https://www.youtube.com/watch?v=T17BTNKBeJY"""
from pathlib import Path


caminho_projeto = Path()
print(caminho_projeto.absolute(), '\n')

caminho_arquivo = Path(__file__)

caminho_pasta = Path.home() / 'Desktop' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True)
print(caminho_pasta)
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir()
print(subpasta, '\n')

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
print(outro_arquivo)
outro_arquivo.write_text('Hey')
print(outro_arquivo.read_text(), '\n')

mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch()
print(mais_arquivo)
mais_arquivo.write_text('Hey')
print(mais_arquivo.read_text(), '\n')
