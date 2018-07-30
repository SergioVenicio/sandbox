import sys
from dis import dis

sys.setrecursionlimit(100000)


class MyInt:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyInt(self.value + other.value)

    def __mul__(self, value):
        return MyInt(self.value * value)


def fat(n):
    return 1 if n <= 1 else n * fat(n-1)


a = MyInt(5)
print(fat(a.value))

dis(fat.__code__.co_code)
