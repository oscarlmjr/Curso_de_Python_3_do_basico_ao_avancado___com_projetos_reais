import enum


Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])
print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
print(Direcoes(1).name, Direcoes.ESQUERDA.value)


def mover(direcao):
	if not isinstance(direcao, Direcoes):
		raise ValueError('Direção não encontrada')
		
	print(f'Movendo para {direcao}')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
# mover('lado')
