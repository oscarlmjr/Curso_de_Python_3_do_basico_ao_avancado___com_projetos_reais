# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os


caminho = os.path.join('D:\\', 'Desenvolvimento', 'Python_3__completo', \
					   'cursopython_prints', 'Section_6__Modulos_Python_' \
					'__os__datetime__sys__json__csv__selenium__pillow_e_mais')
# caminho = os.path.join('D:\\', 'Saved Games')

for pasta in os.listdir(caminho):
	caminho_completo_pasta = os.path.join(caminho, pasta)
	print(pasta)

	if not os.path.isdir(caminho_completo_pasta):
		continue

	for imagem in os.listdir(caminho_completo_pasta):
		print('  ', imagem)
