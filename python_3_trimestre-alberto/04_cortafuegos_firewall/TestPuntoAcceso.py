import unittest,os
from PuntoAcceso import PuntoAcceso, PuntoAccesoError,TipoFiltrado

class TestPuntoAcceso(unittest.TestCase):
    
    os.system('cls')

    def setUp(self) -> None:
        self.punto_acceso = PuntoAcceso("wifi_instituto","hola1234")
        self.equipo1 = 'AB:AC:AD:AE:AF:AG'
        self.equipo2 = 'A1:AC:AD:AE:AF:AG'
        self.equipo3 = 'A2:AC:AD:AE:AF:AG'
        self.equipo4 = 'A3:AC:AD:AE:AF:AG'
        self.equipo5 = 'A4:AC:AD:AE:AF:AG'

    def test_init(self):

        punto_acceso = PuntoAcceso("wifi_instituto","hola1234")    
        self.assertIsInstance(self.punto_acceso,PuntoAcceso)
            #afirmo que la variable punto_acceso almacena algo que hay en la clase PuntoAcceso.                
        self.assertEqual(self.punto_acceso.ssid,"wifi_instituto")
        self.assertEqual(self.punto_acceso.password,"hola1234")
        self.assertListEqual(self.punto_acceso.equipos_conectados, [])
        self.assertFalse(self.punto_acceso.esta_cortafuegos_activado)
        self.assertEqual(self.punto_acceso.tipo_filtrado, TipoFiltrado.LISTA_BLANCA)
        self.assertEqual(self.punto_acceso.equipos_filtrados, [])


    def test_getter_ssid(self):
        self.assertEqual(self.punto_acceso.ssid,"wifi_instituto")


    def test_getter_password(self):    
        self.assertEqual(self.punto_acceso.password,"hola1234")


    def test_esta_cortafuegos_activado(self):
        self.assertFalse(self.punto_acceso.esta_cortafuegos_activado)
    

    def test_desactivar_cortafuegos(self):    
        self.punto_acceso.activar_cortafuegos
        self.punto_acceso.desactivar_cortafuegos
        self.assertFalse(self.punto_acceso.esta_cortafuegos_activado)


    def test_activar_cortafuegos(self):    
        self.punto_acceso.activar_cortafuegos()
        self.assertTrue(self.punto_acceso.esta_cortafuegos_activado)
    

    def test_agregar_equipo_filtrado(self):
        self.assertListEqual(self.punto_acceso.equipos_filtrados, [])
        self.punto_acceso.agregar_equipo_filtrado(self.equipo1)
        self.assertListEqual(self.punto_acceso.equipos_filtrados, [self.equipo1])
        self.punto_acceso.agregar_equipo_filtrado(self.equipo2)
        self.assertListEqual(self.punto_acceso.equipos_filtrados,[self.equipo1,self.equipo2])


    def test_conectar_equipo(self):
        self.punto_acceso.conectar_equipo(self.equipo1,"hola1234")
        self.assertListEqual(self.punto_acceso.equipos_conectados,[self.equipo1])
        self.punto_acceso.conectar_equipo(self.equipo2,"hola1234")
        self.assertListEqual(self.punto_acceso.equipos_conectados,[self.equipo1,self.equipo2])

        with self.assertRaises(PuntoAccesoError):
            self.punto_acceso.conectar_equipo(self.equipo3,"hola5678")
            self.assertListEqual(self.punto_acceso.equipos_conectados,[self.equipo1,self.equipo2])

        self.punto_acceso.activar_cortafuegos()
        # Ahora estamos con lista blanca al activar el cortafuegos 
        # (hemos puesto predefinida la lista blanca cuando encendemos cortafuegos)
        with self.assertRaises(PuntoAccesoError):
            self.punto_acceso.conectar_equipo(self.equipo3,"hola1234")
            self.assertListEqual(self.punto_acceso.equipos_conectados,[self.equipo1,self.equipo2])

        #Añadimos equipo3 a la lista blanca y por lo tanto ya se puede conectar
        self.punto_acceso.agregar_equipo_filtrado(self.equipo3)
        self.punto_acceso.conectar_equipo(self.equipo3,"hola1234")
        self.assertListEqual(self.punto_acceso.equipos_conectados,[self.equipo1,self.equipo2,self.equipo3])

        self.punto_acceso.tipo_filtrado = TipoFiltrado.LISTA_NEGRA
        #AHORA ESTAMOS CON LISTA NEGRA

        #no hay que agregar el equipo filtrado porque sino lo estamos añadiendo a la blacklist y no entra
        self.punto_acceso.conectar_equipo(self.equipo4,"hola1234")
        self.assertListEqual(self.punto_acceso.equipos_conectados,[self.equipo1,self.equipo2,self.equipo3,self.equipo4])
        
        self.punto_acceso.agregar_equipo_filtrado(self.equipo5)
        with self.assertRaises(PuntoAccesoError):
            self.punto_acceso.conectar_equipo(self.equipo5,"hola1234")
            self.assertListEqual(self.punto_acceso.equipos_conectados,[self.equipo1,self.equipo2])




if __name__ == '__main__':
    unittest.main()