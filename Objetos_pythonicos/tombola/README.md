# TDD da Tombola (Python pro)

Uma tombola pode ser criada da seguinte maneira:

```python
    >>> from Objetos_pythonicos.tombola import tombola
    >>> t = tombola.Tombola()

```
Uma lista recém criada não possui elementos. Portanto o método "carregada"
retorna falso:
```python
    >>> itens = [1, 2, 3]
    >>> t.carregada()
    False

```
Após a criação os items da tômbola são representados por uma lista vazia:

```python
    >>> t.itens
    []
    >>> t.carregar(itens)
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
    >>> t()
    1
    >>> t.carregada()
    True

```

O principal método da tombola é sortear. Portanto, se invocada diretamente ela executa esse método
```python
    >>> t()
    2
    >>> t.carregada()
    True
    >>> t()
    3
    >>> t.carregada()
    False
    >>> itens == [1, 2, 3]
    True

```