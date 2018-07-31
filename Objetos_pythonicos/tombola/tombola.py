from random import shuffle

class Tombola:
    def __init__(self):
        self.itens = []

    def carregar(self, itens):
        self.itens = itens
        return self.itens

    def carregada(self):
        return bool(self.itens)

    def misturar(self):
        shuffle(self.itens)

    def sortear(self):
        return self.itens.pop()
