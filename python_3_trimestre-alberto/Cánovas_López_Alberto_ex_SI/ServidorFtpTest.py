import unittest
from ServidorFtp import ServidorFtp

class ServidorFtpTest(unittest.TestCase):

    def test_init(self):
        servidor = ServidorFtp(1000)
        self.assertIsInstance(servidor,ServidorFtp)
    
    def test_obtener_nombre_usuario(self):
        ...




if __name__ == '__main__':
    unittest.main()