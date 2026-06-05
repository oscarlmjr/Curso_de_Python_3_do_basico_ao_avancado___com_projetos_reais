# uma_string: str = 'Um valor'
# uma_inteiro: int = 123456
# uma_float: float = 1.23
# uma_boolean: bool = True
# uma_set: set = {1, 2, 3}
# uma_lista: list = []
# uma_tupla: tuple = 1, 2, 3
# uma_dicionario: dict = {}

# def soma(x: int, y: int, z: float) -> float:
#     return x + y

# lista_inteiros: list[int] = [1, 2, 3, 4, 'a']
# lista_strings: list[str] = ["a", "b", "c", "d"]
# lista_tuplas: list[tuple] = [(1, "a"), (2, "b")]
# lista_listas_int: list[list[int]] = [[1], [4, 5]]

# um_dict: dict[str, int] = {
#     "A": 0,
#     "B": 0,
#     "C": 0,
# }

# um_dict_de_listas: dict[str, list[int]] = {
#     "A": [1, 2],
#     "B": [3, 4],
#     "C": [5, 6],
# }

# um_set_de_inteiros: set[int] = {1, 2, 3}

# ListaInteiros = list[int]
# DictListaInteiros = dict[str, ListaInteiros]

# um_dict_de_listas: DictListaInteiros = {
#     "A": [1, 2],
#     "B": [3, 4],
#     "C": [5, 6],
# }

# string_e_inteiros: str | int = 1  # Union
# string_e_inteiros = "A"  # sem erros
# string_e_inteiros = 2  # sem erros
# lista: list[int | str] = [1, 2, 3, 'a']

# def soma(x: int, y: float | None = None) -> float:
#     if isinstance(y, float | int):
#         return x + y
#     return x + x


# print(soma(1, 10))

# from collections.abc import Callable

# SomaInteiros = Callable[[int, int], int]


# def executa(func: SomaInteiros, a: int, b: int) -> int:
#     return func(a, b)


# def soma(a: int, b: int) -> int:
#     return a + b


# def soma2(a: int, b: float) -> float:
#     return a + b


# executa(soma2(1, 2))

# from typing import TypeVar

# T = TypeVar('T')


# def get_item(list: list[T], index: int) -> T:
#     return list[index]


# list_int = get_item([1, 2, 3],  1)  # int
# list_str = get_item(['a', 'b', 'c'], 1)  # str


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"


def say_my_name(person: Person) -> list[Person]:
    return [person, person]


print(say_my_name(Person("John", "Doe")))
print(say_my_name('asdf'))
