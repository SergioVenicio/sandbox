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