import unittest
from Usuario import Usuario,UsuarioError

class UsuarioTest(unittest.TestCase):

    def test_init(self):
        usuario = Usuario('alberto.canovas','Hola1234','Alberto Cánovas')
        self.assertIsInstance(usuario, Usuario)
        self.assertTrue(Usuario('alberto.canovas','Hola1234','Alberto Cánovas'))

    def test_password(self):
        #self.assertTrue(Usuario.correct_password('Hola1234'))
        ...


if __name__ == '__main__':
    unittest.main()