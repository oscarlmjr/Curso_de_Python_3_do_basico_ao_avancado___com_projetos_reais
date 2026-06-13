from dataclasses import dataclass


@dataclass(repr=False)
class Pessoa:
	nome: str
	sobrenome: str


if __name__ == '__main__':
	p1 = Pessoa('Maria', 'Helena')
	print(p1)
