import unittest
from PuntoAcceso import PuntoAcceso, PuntoAccesoError


class TestPuntoAcceso(unittest.TestCase):

    def test_init(self):
        punto_acceso = PuntoAcceso('wifi_pepe','12345')
        self.assertIsInstance(punto_acceso, PuntoAcceso)
        self.assertEqual(punto_acceso.ssid, 'wifi_pepe')
        self.assertEqual(punto_acceso.contraseña, '12345')
        self.assertListEqual(punto_acceso.equipos_conectados, [])

    def test_conectar(self):
        punto_acceso = PuntoAcceso('wifi_pepe','12345')
        
        self.assertListEqual(punto_acceso.equipos_conectados, [])
        
        punto_acceso.conectar('AA:BB:CC:DD:EE:FF','12345')
        self.assertListEqual(punto_acceso.equipos_conectados,['AA:BB:CC:DD:EE:FF'])
        
        punto_acceso.conectar('AA:BB:CC:DD:EE:F1','12345')
        self.assertListEqual(punto_acceso.equipos_conectados,['AA:BB:CC:DD:EE:FF','AA:BB:CC:DD:EE:F1'])
        
        #cuando se añaden raises se tiene que poner el .assertRaises para comprobar la excepción del código que tiene la contraseña mal, en este caso.
        with self.assertRaises(PuntoAccesoError):
            punto_acceso.conectar('AA:BB:CC:DD:EE:F2','123456')

        self.assertListEqual(punto_acceso.equipos_conectados,['AA:BB:CC:DD:EE:FF','AA:BB:CC:DD:EE:F1'])
        
                                    

if __name__ == '__main__':
    unittest.main()