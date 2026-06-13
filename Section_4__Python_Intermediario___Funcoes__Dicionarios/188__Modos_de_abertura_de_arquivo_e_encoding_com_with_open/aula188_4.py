# Leia também: https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/
# with open (context manager) e métodos úteis do TextIOWrapper
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)

caminho_arquivo = 'D:\\Desenvolvimento\\curso_python\\secao_4\\188__Modos_de_abertura_de_arquivo_e_encoding_com_with_open\\'
caminho_arquivo += 'aula188.txt'

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
	arquivo.write('Atenção\n')
	arquivo.write('Linha 1\n')
	arquivo.write('Linha 2\n')
	arquivo.writelines(('Linha 3\n', 'Linha 4\n'))
