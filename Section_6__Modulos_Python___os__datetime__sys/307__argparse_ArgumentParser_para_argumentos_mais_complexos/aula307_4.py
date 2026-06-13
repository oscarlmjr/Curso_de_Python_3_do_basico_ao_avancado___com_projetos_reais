# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('-b', '--basic')
args = parser.parse_args()
print(args.basic, '\n')

if args.basic is None:
    print('Você não passou o valor de basic.')
else:
    print('O valor de basic:', args.basic)

