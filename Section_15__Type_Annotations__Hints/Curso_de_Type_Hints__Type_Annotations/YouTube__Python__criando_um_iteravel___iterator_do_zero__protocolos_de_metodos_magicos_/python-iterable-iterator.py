class MinhaLista:
    def __init__(self):
        self.__data = {}
        self.__index = 0
        self.__next_index = 0

    def add(self, *values):
        for value in values:
            self.__data[self.__index] = value
            self.__index += 1

    def __check_index(self, index):
        if not self.__data.get(index):
            raise IndexError(f'Index {index} does not exist.')

    def __setitem__(self, index, value):
        self.__check_index(index)
        self.__data[index] = value

    def __getitem__(self, index):
        self.__check_index(index)
        return self.__data[index]

    def __delitem__(self, index):
        self.__check_index(index)
        self.__data[index] = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__next_index >= self.__index:
            self.__next_index = 0
            raise StopIteration

        value = self.__data.get(self.__next_index)
        self.__next_index += 1
        return value

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.__data})'


if __name__ == '__main__':
    lista = MinhaLista()

    lista.add('Maria', 'João')
    lista.add('Helena')
    lista.add('Júlia')

    lista[0] = 'Pedro'
    del lista[0]

    for item in lista:
        print(item)

    for item in lista:
        print(item)

    print(lista)
    