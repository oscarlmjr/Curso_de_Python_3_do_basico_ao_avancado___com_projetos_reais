# https://docs.google.com/spreadsheets/d/12rqI74CeTuCx-E0hlGuVbK8EHqw98couYbdfoW9EwIk/edit?gid=96103348#gid=96103348
# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path


CAMINHO_CSV = Path(__file__).parent / 'aula293.csv'

with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
# with open(CAMINHO_CSV, 'r') as arquivo:
	leitor = csv.DictReader(arquivo)

	for linha in leitor:
		print(linha['Nome'], linha['Idade'], linha['Endereço'])

	leitor = csv.reader(arquivo)

	for linha in leitor:
		print(linha)
