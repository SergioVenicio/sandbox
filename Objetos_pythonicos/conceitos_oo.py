# Objetos mutaveis: dict, list, set
# Objetos imutaveis: str, int, float, tupla, frozenset
# Aliasing: Apelidamento, EX: Edson -> Pelé (Varios nomes para o mesmo Obj)
# Variáveis são rotulos e o valor está em caixas

# Ex
a = [1, 2, 3]

b = a


print(id(a) == id(b))


# Iteração -> Iterators, Iterable e Generetors

# Iterators EX:
import sys


for arg in sys.args:
    print(arg)

# List Comprehensions
# Consomem iteráveis e produzem listas
s = 'abracadabra'
l = [ord(c) for c in s]
[ord(c) for c in s]

# SET e Dict Comprehensions
s = 'abracadabra'

# Set comprehension
{c for c in s}

# Dict Comprehension
{c: ord(c) for c in s}


# Iterável: Pode ser iterado
# Range retorna um iteravel
numeros = list(range(10))
[n * 2 for n in numeros]
list(map(lambda n: n * 2, numeros))

# Protocolo de sequencia
# -- Iteraveis embutidos

# --- Mutáveis
    # list, dict, set, deque
# --- Imutaveis
    # tuple, frozenset, srt, bytes, file, range

# Funções consumidoras
# all, any, filter, iter, map, len, max, min, reduce, sorted, sum, zip

# all retorna true se todos os itens retornarem True se não False
# Ex
b = [True, True, True, False]

all(b) # False

# Any retorna True se dentro dos itens existir um True
any(b) # True

# Função que verifica se todos os numeros são pares
all(map(lambda x: True if not x % 2 else False), [2, 4, 6, 8])

# MAP OBJ (Não aloca espaço em memória)
l = [0, 1, 2, 3, 4, 5, 6, 7, 8]
q_menos_1 = map(lambda n: n ** 2 -1, l)
q_menos_1 # <map object> Iterável, porem não é uma lista
all(map(lambda n: n == 63), q_menos_1)

# List comprehension
# Remover os numeros pares
[n for n in l if n % 2 == 1]
    # Filter
# Adiciona na lista caso o filtro retorne True
a = filter(lambda n: n % 2 == 1, l) # <filter object>
list(a) # para transformar em lista


# ZIP (zip_longest vai até o final do mais e defini como none -> filvalue)
paises = ['en', 'br', 'es']
linguas = ['Ingles', 'Portugues', 'Espanhol']

paises = list(zip(paises, linguas))
for pais, lingua in paises:
    print(pais, lingua)


# O que é um iteravel ?
# Objeto no qual a função iter obtém um iterador (__iter__), caso a função não tenha __iter__ o interpretador tenta obj[0], obj[1]
# Protocolo de sequência
from collections import Sequence # Class Abstrata (Interface)

class Trem(Sequence):
    def __init__(self, num_vagoes):
        self.num_vagoes = num_vagoes

    def __len__(self):
        return self.num_vagoes

    def __getitem__(self, item):
        indice = item if item >= 0 else self.num_vagoes + item
        if 0 <= indice < self.num_vagoes:
            return f'Vagao {indice + 1}'
        raise IndexError(f'Vagao inexistente {item}')


for vagao in Trem(4):
    print(vagao)



# Trem com iterator
class Trem:
    def __init__(self, num_vagoes):
        self.num_vagoes = num_vagoes

    def __iter__(self):
        return IteradorTrem(self.num_vagoes)


class IteradorTrem(object):
    def __init__(self, num_vagoes):
        self.atual = 0
        self.ultimo_vagao = num_vagoes - 1

    def __next__(self):
        if self.atual <= self.ultimo_vagao:
            self.atual += 1
            return f'vagao {self.atual}'

        raise StopIteration()


for vagao in Trem(4):
    print(vagao)


# Geradores
# # Enumerate
enumerate(l) # <enumerate object>


# Função geradora (Generetors)
# Qualquer função com a palavra reservada yeild (retorna um objeto gerador)
def geradora():
    for i in range(3):
        yield i

# List generetor
(i for i in range(3))


# Exercicio
class Arvore:
    def __init__(self, valor, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita


    def __iter__(self):
        if self.esquerda is not None:
            yield from self.esquerda

        yield self.valor

        if self.direita is not None:
            yield from self.direita



Arvore(0, Arvore(-2, Arvore(-4), Arvore(-1)), Arvore(10))