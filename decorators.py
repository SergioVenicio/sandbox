import functools
from abc import ABC, abstractmethod

# Semântica de propriedade
class Bicicleta(ABC):
    def __init__(self):
        self._velocidade = 0

    @property
    @abstractmethod
    def marca(self):
        return self._marca

    @marca.setter
    @classmethod
    def marca(cls, marca):
        cls._marca = marca

    @staticmethod
    def rodas():
        # método de classe.
        return 2

    @property
    def velocidade(self):
        # property retorna o valor de um método como atributo
        return self._velocidade

    @velocidade.setter
    def velocidade(self, valor):
        # x.setter seta o valor de um atributo
        if valor > 0:
            self._velocidade = valor
        else:
            self._velocidade = 0

    @abstractmethod
    def pedalar(self):
        raise NotImplementedError

    @abstractmethod
    def frear(self):
        raise NotImplementedError


class Monark(Bicicleta):
    marca = 'Monark'

    def pedalar(self):
        self.velocidade += 5

    def frear(self):
        self.velocidade -= 6


class Caloi(Bicicleta):
    marca = 'Caloi'

    def pedalar(self):
        self.velocidade += 6

    def frear(self):
        self.velocidade -= 5


bicicleta = Monark()
bicicleta.pedalar()
bicicleta.frear()
bicicleta.frear()
bicicleta.frear()
bicicleta.frear()
bicicleta.frear()
print(bicicleta.velocidade)
print(bicicleta.marca)


bicicleta = Caloi()
bicicleta.pedalar()
bicicleta.frear()
bicicleta.frear()
bicicleta.frear()
bicicleta.frear()
print(bicicleta.velocidade)
print(bicicleta.marca)



# Decoradores de classe
@functools.total_ordering
class Aluno:
    def __init__(self, nota):
        self.nota = nota

    def __eq__(self, other):
        if isinstance(other, Aluno):
            return self.nota == other.nota
        else:
            False

    def __lt__(self, other):
        return self.nota < other.nota

    # def __gt__(self, other):
    #     return self.nota > other.nota
    #
    # def __ge__(self, other):
    #     return  self.nota >= other.nota
    #
    # def __le__(self, other):
    #     return self.nota <= other.nota


aluno_10 = Aluno(10)
aluno_2_10 = Aluno(10)
aluno_1 = Aluno(1)


print(aluno_10 == aluno_2_10)
print(aluno_10 == aluno_1)
print(aluno_10 > aluno_1)
print(aluno_10 < aluno_1)
print(aluno_10 >= aluno_1)
print(aluno_10 <= aluno_1)