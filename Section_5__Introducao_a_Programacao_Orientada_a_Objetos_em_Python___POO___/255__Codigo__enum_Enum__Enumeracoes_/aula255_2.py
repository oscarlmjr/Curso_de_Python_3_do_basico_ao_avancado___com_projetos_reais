import enum


Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

def mover(direcao):
	if not isinstance(direcao, Direcoes):
		raise ValueError('Direção não encontrada')
		
	print(f'Movendo para {direcao}')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover('lado')
