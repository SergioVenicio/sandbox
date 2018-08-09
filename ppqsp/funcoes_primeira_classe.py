# Funções são objetos
# Funçoes podem ser manipuladas como outros objetos
    # Criar em tempo de execução
    # Atribuição
    # Passagem como argumento
    # Armazenamento em estrutura de dados
    # Retorno de funções


import pytest
from dis import dis # disasembly

def fatorial(n):
    return 1 if n < 2 else fatorial(n - 1) * n

@pytest.mark.parametrize('n, esperado',[
    (1, 1), (2, 2), (3, 6), (4, 24), (5, 120)
])
def test_fatorial(n, esperado):
    assert esperado == fatorial(n)

def test_atribuicao_de_funcao():
    fat = fatorial
    assert 120 == fat(5)
    assert fat is fatorial
    assert 'fatorial' == fat.__name__




def divisao_inteira(divisor, quociente):
    return divisor // quociente


# Funções de primeira classe (retorna uma função)
def criar_divisao(quociente):
    def divisao_por_quociente(n):
        return divisao_inteira(n, quociente)

    return divisao_por_quociente

if __name__ == '__main__':
    fat = fatorial

    # __code__ : caracteristicas do código da função
    print(fat.__code__)
    dis(fat.__code__.co_code)

    # Retorna um tipo map, mais rápido que uma lista normal
    results = map(fat, range(1, 5))
    for r in results:
        print(r)


    div_2 = criar_divisao(2)
    print(div_2(10))

    div_3 = criar_divisao(3)
    print(div_3(15))
