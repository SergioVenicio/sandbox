from dataclasses import dataclass
from decimal import Decimal, getcontext

getcontext().prec = 6


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int
    sexo: str


@dataclass
class Cliente(Pessoa):
    numero: int


@dataclass
class Conta:
    numero: int
    saldo: Decimal
    depositos: list
    saques: list

    def _valor_positivo(self, valor):
        if valor > 0:
            return True

        return False

    def depositar(self, valor):
        if self._valor_positivo(valor):
            self.saldo += Decimal(valor)
            self.depositos.append(valor)

    def sacar(self, valor):
        if self._valor_positivo(valor) and self.saldo >= valor:
            self.saldo -= Decimal(valor)
            self.saques.append(valor)
