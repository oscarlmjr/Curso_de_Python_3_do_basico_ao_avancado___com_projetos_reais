"""https://www.youtube.com/watch?v=T17BTNKBeJY"""
from pathlib import Path


caminho_projeto = Path()
print(caminho_projeto.absolute(), '\n')

caminho_arquivo = Path(__file__)

print(Path.home())
print(Path.home() / 'Desktop', '\n')

caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
# caminho_arquivo.unlink()
caminho_arquivo.touch()   # subscreve
caminho_arquivo.write_text('')

with caminho_arquivo.open('a+') as file:
	file.write('Uma linha\n')
	file.write('Outra linha\n')

print(caminho_arquivo.read_text())
