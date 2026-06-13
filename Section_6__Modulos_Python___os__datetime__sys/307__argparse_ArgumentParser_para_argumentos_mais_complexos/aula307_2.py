# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser


parser = ArgumentParser()

parser.add_argument('-b')
args = parser.parse_args()
print(args.b, '\n')

if args.b is None:
    print('Você não passou o valor de b.')
else:
    print('O valor de b:', args.b)

