# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho em uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
import os


caminho = os.path.join('\\home\\users', 'Desktop', 'curso', 'arquivo.txt')
print(caminho)
caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
print(caminho)
diretorio_arquivo = os.path.split(caminho)
print(diretorio_arquivo)

diretorio, arquivo = os.path.split(caminho)
print(diretorio, arquivo)
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(nome_arquivo, extensao_arquivo)
caminho_arquivo, extensao_arquivo = os.path.splitext(caminho)
print(caminho_arquivo, extensao_arquivo)
print(os.path.exists(caminho))
print(os.path.exists('D:\\Desenvolvimento\\Python_3__completo'))
print(os.path.abspath('.'))
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(caminho))
