import unittest
from Baraja import Baraja
from Carta import Carta, Palo,ValorCarta


class BarajaTest(unittest.TestCase):
    def test_init(self):

        #inicializamos y creamos el objeto
        baraja = Baraja()
        
        #decimos que el objeto baraja es del tipo Baraja
        self.assertIsInstance(baraja,Baraja)

        lista_comprobacion = []
        #recorremos todos los palos, uno a uno
        for palo in Palo:
            #durante los 12 números de valor de la carta
            for valor in range(1,13):
                #añadimos el objeto Carta, con los valores y palo que va recorriendo el bucle en la lista_comprobacion
                lista_comprobacion.append(Carta(valor,palo))

        #comparamos que la lista de baraja sea la misma que la lista de comprobación
        self.assertListEqual(baraja, lista_comprobacion)






if __name__ == '__main__':
    unittest.main()