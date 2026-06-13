import os

# Leia também: https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/
# with open (context manager) e métodos úteis do TextIOWrapper
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)

caminho_arquivo = 'D:\\Desenvolvimento\\curso_python\\secao_4\\189__os_remove__os_unlink_e_os_rename___apagando__renomeando_e_movendo_arquivos\\'
caminho_arquivo += 'aula189.txt'

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
	arquivo.write('Atenção\n')
	arquivo.write('Linha 1\n')
	arquivo.write('Linha 2\n')
	arquivo.writelines(('Linha 3\n', 'Linha 4\n'))

os.rename(caminho_arquivo, 'aula189_renamed.txt')
# renomea o arquivo anterior na open folder ou mantém o arquivo
# anterior na pasta origem e cria novo arquivo renomeado na open folder
