from collections import deque


# Seguencia mutável
# Generalizaçaõ entre uma lista/pilha/fila
# É uma lista

class Fila:
    def __init__(self):
        self.lista = deque()

    def insert(self, value):
        self.lista.append(value)

    def remove(self):
        if self.lista:
            return self.lista.popleft()


    def __repr__(self):
        return 'Fila[{}]'.format(
            ', '.join(str(x) for x in self.lista)
        )


class Pilha:
    def __init__(self):
        self.lista = deque()

    def insert(self, value):
        self.lista.append(value)

    def pop(self):
        if self.lista:
            return self.lista.pop()

    def __repr__(self):
        return 'Pilha[{}]'.format(
            ', '.join(str(x) for x in self.lista)
        )



from collections import namedtuple


# Jogador = namedtuple('Jogador', ['nome', 'time', 'camisa', 'numero'])

# ronaldo = Jogador('Ronaldo', 'Corintia', 9, 6565)


# n = namedtuple('ABC', 'slot1 slot2 slot3'.split())

naipes = 'P C O E'.split()
valores = list(range(2, 11)) + 'A J Q K'.split()

carta = namedtuple('Carta', ['naipe', 'valor'])

baralho = [
    carta(naipe, valor)
    for naipe in naipes
    for valor in valores
]