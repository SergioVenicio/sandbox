class Mamifero:
    pass


class GrandeMixin:
    def latir(self, vezes=1):
        print(f'{self.nome}: ' + 'Wuff! ' * vezes)


class Cao(Mamifero):
    tamanho = 'Pequeno'
    qtd_patas = 4
    nervoso = False

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

    def __repr__(self):
        return f'Cao({self.nome})'

    def __eq__(self, other):
        return (isinstance(other, Cao) and
                self.__dict__ == other.__dict__)

    def latir(self, vezes=1):
        vezes = vezes + (self.nervoso * vezes)
        print(f'{self.nome}: ' + 'AU! ' * vezes)


class Pequines(Cao):
    """
        >>> fido = Pequines('Fido')
        >>> fido.latir()
        Fido: AU! AU!

    """
    nervoso = True


class PastorAlemao(GrandeMixin, Cao):
    """
        >>> alemao = PastorAlemao('Alemao')
        >>> alemao.latir()
        Alemao: Wuff!
    """

    tamanho = 'Grande'

    def __init__(self, nome):
        Cao.__init__(self, nome)
