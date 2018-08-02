# Definem protocolos da linguagem python

# Objetos invocáveis
# Toda função é um objeto invocável (__call__)
# EX
import math
from Objetos_pythonicos.tombola.tombola import Tombola

t = Tombola()
t.carregar([item for item in range(5)])
# Chama o método principal da classe (sortear())
t()


# Sobrecarga de operadores
# Classes definidas pelo usuário, podem sobrecarregar operadores
# Não é possivel fazer isso em tipos embutidos (builtins)
# EX
# Aritiméticos: + - * ** //
# Bitwise: & ^| << >>
class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        if isinstance(other, Vetor):
            return Vetor(self.x + other.x, self.y + other.y)
        return Vetor(self.x + other, self.y + other)

    def __iadd__(self, other):
        if isinstance(other, Vetor):
            self.x += other.x
            self.y += other.y
        else:
            self.x + other
            self.y + other

        return self

    def __radd__(self, other):
        if isinstance(other, Vetor):
            return Vetor(self.x + other.x, self.y + other.y)
        return Vetor(self.x + other, self.y + other)

    def __mul__(self, other):
        if isinstance(other, Vetor):
            return Vetor(self.x * other.x, self.y * other.y)

        return Vetor(self.x * other, self.y * other)

    def __rmul__(self, other):
        if isinstance(other, Vetor):
            return Vetor(self.x * other.x, self.y * other.y)

        return Vetor(self.x * other, self.y * other)

    def __matmul__(self, other):
        if isinstance(other, Vetor):
            return Vetor(self.x * other.x, self.y * other.y)

        return Vetor(self.x * other, self.y * other)

    def __repr__(self):
        return f'Vetor({self.x}, {self.y})'


vetor = Vetor(3, 4)
vetor2 = Vetor(1, 1)
print(abs(vetor))
print(vetor + vetor2)
print(2 + vetor2)
print(abs(vetor + vetor2))
print(id(vetor))
vetor += vetor2
print(vetor)
print(id(vetor))
print(vetor * 2)
print(2 * vetor)
print(vetor @ Vetor(8, 8))