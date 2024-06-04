import unittest

from Usuario import Usuario, UsuarioError

class UsuarioTest(unittest.TestCase):

    def setUp(self) -> None:
        self.usuario = Usuario('lucia.perez', 'Hola1234', 'Lucia Perez')
        
    #este método es para evitar crear el objeto en todas las pruebas
    #tenemos que añadir el self. delante de todos los objetos cuando los llamamos

    
    def test_init(self):
        self.assertIsInstance(self.usuario,Usuario)
        self.assertEqual(self.usuario.login,'lucia.perez')
        self.assertEqual(self.usuario.nombre_completo, 'Lucia Perez')
        #no se puede poner el assertEqual de contraseña porque no hay getter 
        #si ponemos .__contraseña nos da error porque es privado y no podemos acceder

        with self.assertRaises(UsuarioError):
            usuario2 = Usuario('ruben.martinez','Hola','Ruben Martinez')
        #el objeto usuario2 está mal porque la contraseña no tiene 8 caracteres

    def test_getter_login(self):
        self.assertEqual(self.usuario.login,'lucia.perez')
        
    
    def test_getter_nombre_completo(self):
        self.assertEqual(self.usuario.nombre_completo, 'Lucia Perez')


    def test_setter_nombre_completo(self):
        self.assertEqual(self.usuario.nombre_completo, 'Lucia Perez')
        self.usuario.nombre_completo = 'Susana Lopez'
        self.assertEqual(self.usuario.nombre_completo,'Susana Lopez')
    
    
    def test_es_contraseña_compleja(self):
        self.assertTrue(Usuario.es_contraseña_compleja('Hola1234'))
        #como es estático el método ponemos el nombre de la clase delante Usuario.
        self.assertFalse(Usuario.es_contraseña_compleja('Hola123'))
        self.assertTrue(Usuario.es_contraseña_compleja('Hola12345'))

    def test_supera_autenticacion(self):
        self.assertTrue(self.usuario.supera_autenticacion('Hola1234'))
        self.assertFalse(self.usuario.supera_autenticacion('Hola12345'))
        
        #siempre que es boleano devolvemos una prueba true y otra false




if __name__ == '__main__':
    unittest.main()
    
    #boilerplate