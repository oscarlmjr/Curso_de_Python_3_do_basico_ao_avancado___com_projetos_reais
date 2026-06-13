# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil


HOME = os.path.expanduser('~')
print(HOME)
DESKTOP = os.path.join(HOME, 'Desktop')
print(DESKTOP)
PASTA_ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO')
print(PASTA_ORIGINAL)
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')
print(NOVA_PASTA)
