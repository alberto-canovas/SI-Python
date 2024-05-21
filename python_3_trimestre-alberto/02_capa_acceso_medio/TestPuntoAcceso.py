import unittest
from PuntoAcceso import PuntoAcceso,TipoWifi


class TestPuntoAcceso(unittest.TestCase):

    def test_init(self):
        punto_acceso = PuntoAcceso("wifi_ññ","hola1234",[TipoWifi.WIFI5])
        self.assertIsInstance(punto_acceso, PuntoAcceso)

    def test_getter_ssid(self):
        punto_acceso = PuntoAcceso("wifi_ññ","hola1234",[TipoWifi.WIFI5])
        self.assertEqual(punto_acceso.ssid, "wifi_ññ")

    def test_getter_password(self):
        punto_acceso = PuntoAcceso("wifi_ññ","hola1234",[TipoWifi.WIFI5])
        self.assertEqual(punto_acceso.password,"hola1234")

    def test_getter_tipos_wifi(self):
        punto_acceso = PuntoAcceso("wifi_ññ","hola1234",[TipoWifi.WIFI4,TipoWifi.WIFI5])
        self.assertListEqual(punto_acceso.tipos_wifi, [TipoWifi.WIFI4,TipoWifi.WIFI5])

    def test_setter_password(self):
        punto_acceso = PuntoAcceso("wifi_ññ","hola1234",[TipoWifi.WIFI5])
        punto_acceso.password = 'adios4321'
        self.assertEqual(punto_acceso.password, 'adios4321')

    def test_setter_ssid(self):
        punto_acceso = PuntoAcceso("wifi_ññ","hola1234",[TipoWifi.WIFI5])
        punto_acceso.ssid = 'wifi_españa'
        self.assertEqual(punto_acceso.ssid, 'wifi_españa')

    

if __name__ == '__main__':
    unittest.main()