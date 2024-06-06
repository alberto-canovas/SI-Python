import unittest
from Usuario import Usuario,UsuarioError

class UsuarioTest(unittest.TestCase):

    def setUp(self):
        self.usuario = Usuario('alberto.cano','Hola1234','Alberto Canovas')

    def test_init(self):
        self.assertIsInstance(self.usuario,Usuario)
        self.assertEqual(self.usuario.login,'alberto.cano')
        self.assertEqual(self.usuario.name,'Alberto Canovas')

            

    def test_comprobar_contraseña(self):
        self.assertTrue(self.usuario.comprobar_contraseña('Hola1234'))
        self.assertFalse(self.usuario.comprobar_contraseña('Hola123'))
        self.assertFalse(self.usuario.comprobar_contraseña('Hola12345'))
    
    def test_correct_password(self):
        self.assertTrue(Usuario.correct_password('Hola1234'))
        self.assertTrue(Usuario.correct_password('Hola12345'))
        self.assertFalse(Usuario.correct_password('Hola123'))
        


if __name__ == '__main__':
    unittest.main()