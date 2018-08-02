from itertools import product


def gerar_linha(matriz, n):
    return matriz[n]


def gerar_coluna(matriz, n):
    return [linha[n] for linha in matriz]


class Matriz:
    def __init__(self, lista):
        self.lista = lista

    def __matmul__(self, other):
        lista = self.lista
        o_lista = other.lista
        n_colunas = len(o_lista[0])
        n_linhas = len(lista)
        resultado = [
            [0 for _ in range(n_colunas) ]
            for _ in range(n_linhas)
        ]

        for i, j in product(range(n_linhas), range(n_colunas)):
            _zip_elements = zip(
                gerar_linha(lista, i), gerar_coluna(o_lista, j)
            )
            for el_linha, el_coluna in _zip_elements:
                resultado[i][j] += el_linha * el_coluna

        return Matriz(resultado)

    def __repr__(self):
        return f'Matriz({self.lista})'