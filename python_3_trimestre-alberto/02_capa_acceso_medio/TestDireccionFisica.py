import unittest
from DireccionFisica import DireccionFisica



class TestDireccionFisica(unittest.TestCase):
    
    def test_es_direccion_correcta (self):
        #self.assertFalse(DireccionFisica.es_direccion_correcta())
        self.assertFalse(DireccionFisica.es_direccion_correcta("hola")) #INDICAMOS QUE ES FALSO el "hola" (assert.False)
        self.assertFalse(DireccionFisica.es_direccion_correcta(1))
        self.assertFalse(DireccionFisica.es_direccion_correcta(False))
        self.assertFalse(DireccionFisica.es_direccion_correcta("D0-37-45-DE-01-C3")) 
        self.assertFalse(DireccionFisica.es_direccion_correcta("D0:37:45:DE:01:C3:H5"))
        self.assertFalse(DireccionFisica.es_direccion_correcta("D0:37:45:DE:01:C"))
        self.assertFalse(DireccionFisica.es_direccion_correcta("1234567891234567"))
        self.assertFalse(DireccionFisica.es_direccion_correcta("123456789123456789"))
        #self.assertFalse(DireccionFisica.es_direccion_correcta("D0:37:45:DE:01:C3","D0:37:45:DE:01:C3"))

        self.assertTrue(DireccionFisica.es_direccion_correcta("D0:37:45:DE:01:C3")) #INDICAMOS QUE ES VERDADERO CON EL (assertTrue)
        self.assertTrue(DireccionFisica.es_direccion_correcta("d0:37:45:de:01:c3")) #buena
        
    def test_constructor(self): # Init es lo mismo que constructor. El self significa que es un método.
        direccion1 = DireccionFisica('E5:A3:14:BC:D9:6D')

        with self.assertRaises(Exception): #Afirmamos que algo lanza una excepción(assertRaises)
            direccion2 = DireccionFisica ('G5:A3:14:BC:D9:6D')
            
    def test_getter(self):
        direccion1= DireccionFisica('E5:A3:14:BC:D9:6D')
        self.assertEqual(direccion1.direccion, 'E5:A3:14:BC:D9:6D')

    def test_setter_direccion(self):
        direccion1 = DireccionFisica('E5:A3:14:BC:D9:6D')
        direccion1.direccion = 'A1:A3:A4:A5:A9:6D'
        self.assertEqual(direccion1.direccion, 'A1:A3:A4:A5:A9:6D')

if __name__ == '__main__':
    unittest.main()