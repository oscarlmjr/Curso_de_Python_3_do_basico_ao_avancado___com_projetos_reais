# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser


parser = ArgumentParser()

print(parser, '\n')

parser.add_argument('-b')
args = parser.parse_args()
print(args.b, '\n')
