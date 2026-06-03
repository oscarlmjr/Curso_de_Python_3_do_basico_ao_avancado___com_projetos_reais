# https://docs.python.org/3/library/typing.html

from typing import Sequence, Iterable


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando...')


def iterar(sequencia: Sequence[int]):
    return [x * 2 for x in sequencia]


def iterar2(sequencia: Iterable[int]):
    return [x for x in sequencia]


print(iterar([1, 2, 3]))
print(iterar((1, 2, 3)))
print(iterar2([1, 2, 3]))
print(iterar2((1, 2, 3)))