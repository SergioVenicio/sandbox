from random import shuffle
from itertools import product
from collections import namedtuple

Carta = namedtuple('Carta', 'valor naipe')

class Baralho:
    valores = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    naipes = 'P E C O'.split()

    def __init__(self):
        self.cartas = [
            Carta(v, n) for n, v in product(self.naipes, self.valores)
        ]
        shuffle(self)

    def __len__(self):
        return len(self.cartas)

    def __getitem__(self, item):
        return self.cartas[item]

    def __setitem__(self, key, value):
        self.cartas[key] = value

    def __embaralhar(self):
        shuffle(self.cartas)