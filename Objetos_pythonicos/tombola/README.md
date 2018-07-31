# TDD da Tombola (Python pro)

Uma tombola pode ser criada da seguinte maneira:

```python
    >>> from tombola import tombola
    >>> t = tombola.Tombola()

```
Uma lista recém criada não possui elementos. Portanto o método "carregada"
retorna falso:
```python
    >>> t.carregada()
    False

```
Após a criação os items da tômbola são representados por uma lista vazia:

```python
    >>> t.itens
    []
    >>> t.carregar([1, 2, 3])
    [1, 2, 3]
    

```

Após ser carregada o método "carregada" retorna verdadeiro:

```python
    >>> t.carregada()
    True

```

Uma tômbola pode misturar os seus itens:
```python
    >>> def embaralhador_mock(lista):
    ...     lista[0], lista[-1] = lista[-1], lista[0]
    >>> t.itens
    [1, 2, 3]
    >>> tombola.shuffle = embaralhador_mock
    >>> t.misturar()
    >>> t.itens != [1, 2, 3]
    True

```

Uma tômbola serve para sortear elementos:
```python
    >>> t.sortear()
    1
    >>> t.carregada()
    True
    >>> t.sortear()
    2
    >>> t.carregada()
    True
    >>> t.sortear()
    3
    >>> t.carregada()
    False

```