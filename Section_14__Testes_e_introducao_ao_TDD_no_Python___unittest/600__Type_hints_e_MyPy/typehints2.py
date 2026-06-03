# https://docs.python.org/3/library/typing.html

from typing import Callable


# def retorna_funcao(funcao: Callable[[], None]) -> Callable:
def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao

# def fala_oi():
# 	print('Oi')


# retorna_funcao(fala_oi)()

def soma(x: int, y: int) -> int:
    return x + y


# retorna_funcao(soma)(10, 20)
print(retorna_funcao(soma)(10, 20))

