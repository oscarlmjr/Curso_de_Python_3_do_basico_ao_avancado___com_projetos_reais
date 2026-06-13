# (Parte 3) Threads - Executando processamentos em paralelo
from threading import Lock, Thread
from time import sleep


class Ingressos:

    def __init__(self, estoque):
        self.estoque = estoque

    def comprar(self, quantidade):

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            return

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} em estoque.')


if __name__ == '__main__':
    ingressos = Ingressos(10)
    
    for i in range(1, 10):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)
