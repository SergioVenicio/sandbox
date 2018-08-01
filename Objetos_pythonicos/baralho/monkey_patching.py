# Alteração de classe em tempo de execução.

import baralho


def setitem(self, pos, carta):
    print('Novo setitem')
    self.cartas[pos] = carta


baralho.Baralho.__setitem__ = setitem


b = baralho.Baralho()