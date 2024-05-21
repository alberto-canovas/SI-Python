import unittest

from Conmutador import Conmutador, ConmutadorError
from PuertoRed import PuertoRed, Tecnologia
from DireccionFisica import DireccionFisica

class TestConmutador(unittest.TestCase):
    
    def test_init(self):
        conmutador = Conmutador(10)
        self.assertIsInstance(conmutador, Conmutador)


    def test_cantidad_puertos(self):
        conmutador= Conmutador(10)
        self.assertEqual(conmutador.cantidad_puertos,10) 

    def test_getter_puertos(self):
        conmutador = Conmutador(10) 
        self.assertListEqual(conmutador.puertos, [])

    def test_getter_encendido(self):
        conmutador = Conmutador(10)
        self.assertFalse(conmutador.encendido)


    def test_encender(self):
        conmutador = Conmutador(10)

        conmutador.encender() #al encenderlo ponemos el conmutador en True
        self.assertTrue(conmutador.encendido) #en esta línea afirmamos que está en True (una aserción/afirmación)
        

    def test_encender_apagar(self):

        conmutador = Conmutador(10)
        self.assertFalse(conmutador.encendido)

        conmutador.encender()#primero lo encendemos porque está apagado desde un principio

        conmutador.apagar()#lo apagamos y se cambia el conmutador a False
        self.assertFalse(conmutador.encendido) # afirmamos que está en False
    
    def test_añadir_puerto(self):
        conmutador = Conmutador(4)

        direccion1= DireccionFisica('AA:BB:CC:D1:D5:F6')
        puerto1 =PuertoRed(direccion1,Tecnologia.PAR_TRENZADO_1000)
        conmutador.añadir_puerto(puerto1)
        self.assertEqual(len(conmutador.puertos), 1)
        self.assertListEqual(conmutador.puertos,[puerto1]) # afirmamos que la lista puertos contiene [puerto1]

        conmutador.encender()
        direccion2= DireccionFisica('A3:BB:CC:D1:D5:F6')
        puerto2 =PuertoRed(direccion2,Tecnologia.PAR_TRENZADO_1000)

        with self.assertRaises(ConmutadorError): #afirmamos que se va a lanzar una excepción (porque en la línea 42 encendemos el switch)
            conmutador.añadir_puerto(puerto2)
        
        conmutador.apagar()
        conmutador.añadir_puerto(puerto2)
        self.assertEqual(len(conmutador.puertos), 2)
        self.assertListEqual(conmutador.puertos,[puerto1, puerto2]) # afirmamos que la lista puertos contiene [puerto1, puerto2]
        
        direccion3= DireccionFisica('8A:BB:CC:D1:D5:F6')
        puerto3 =PuertoRed(direccion3,Tecnologia.PAR_TRENZADO_1000)
        conmutador.añadir_puerto(puerto3)
        self.assertEqual(len(conmutador.puertos), 3)
        self.assertListEqual(conmutador.puertos,[puerto1, puerto2, puerto3])
        
        direccion4= DireccionFisica('9A:BB:CC:D1:D5:F6')
        puerto4 =PuertoRed(direccion4,Tecnologia.PAR_TRENZADO_1000)
        conmutador.añadir_puerto(puerto4)
        self.assertEqual(len(conmutador.puertos), 4)
        self.assertListEqual(conmutador.puertos,[puerto1, puerto2, puerto3, puerto4])
        
        direccion5= DireccionFisica('0A:BB:CC:D1:D5:F6')
        puerto5 =PuertoRed(direccion5,Tecnologia.PAR_TRENZADO_1000)
        with self.assertRaises(ConmutadorError): #afirmamos que va a lanzar una excepcion(el switch solo tiene 4 puertos)
            conmutador.añadir_puerto(puerto5)
        





if __name__ == '__main__':
    unittest.main()


