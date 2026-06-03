# https://docs.python.org/3/library/typing.html

from typing import List, Union, Tuple, Dict, Any, NewType


# Primitivos
numero: int = 10
flutuante: float = 10.5
boleano: bool = False
string: str = 'Luiz Otávio'

# Sequências
lista: List[int] = [1, 2, 3]
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Luiz']
tupla: Tuple[int, int, int, str] = (1, 2, 3, 'Luiz')

# Dicionários e conjuntos
# pessoa: Dict = {'nome': 'Luiz Otávio', 'sobrenome': 'Miranda'}
# pessoa: Dict[str, str] = {'nome': 'Luiz Otávio', 'sobrenome': 'Miranda'}
pessoa: Dict[str, Union[str, int]] = {'nome': 'Luiz Otávio', 
			'sobrenome': 'Miranda',	'idade': 30}
pessoa2: Dict[str, Any] = {'nome': 'Luiz Otávio', 
			'sobrenome': 'Miranda',	'idade': 30}
pessoa3: Dict[str, Union[str, int, List[int]]] = {
    'nome': 'Luiz Otávio', 'sobrenome': 'Miranda', 'idade': 30, 'l': [1, 2]}

# Meu tipo
MeuDict =  Dict[str, Union[str, int, List[int]]] # Alias
pessoa4: MeuDict = {'nome': 'Luiz Otávio', 'sobrenome': 'Miranda', 
		'idade': 30, 'l': [1, 2]}

#Meu outro tipo
UserId = NewType ('UserId', int)
user_id = UserId(32654821)