import unittest

from Objetos_pythonicos.tombola import tombola


class Test_Tombola(unittest.TestCase):
    def setUp(self):
        self.itens = [item for item in range(10)]
        self.tombola = tombola.Tombola()
        self.tombola.carregar(self.itens)

    def test_init_tombola(self):
        self.assertEqual(len(self.tombola.itens), 10)
        self.assertTrue(self.tombola.carregada())


    def test_misturar(self):
        self.tombola.misturar()
        self.assertNotEqual(self.tombola.itens, self.itens)


    def test_sortear(self):
        item_sorteado = self.tombola()
        self.assertFalse(item_sorteado in self.tombola.itens)


    def test_sortear_todos(self):
        while self.tombola.itens:
            self.tombola()

        self.assertFalse(self.tombola.itens)