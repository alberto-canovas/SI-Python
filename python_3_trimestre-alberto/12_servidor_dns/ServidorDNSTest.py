from ServidorDNS import DireccionIp,NombreDns, ServidorDns
import unittest

class Alumno:
    def __init__(self,nre:str, nombre: str, apellido: str) -> None:
        self.nre = 1804140
        self.nombre = nombre
        self.apellido = apellido

    def __eq__(self, value: object) -> bool:
        if self.nre == value.nre and self.nombre == value.nombre and self.apellido == value.apellido:
            return True
        else:
            return False
    
    def __repr__(self) -> str: #ES LO MISMO QUE TOSTRING DE JAVA
        return f'[{self.nre}] {self.nombre} {self.apellido}'

class ServidorDnsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.alumnos = []
        alumno1 = Alumno(1804140,'Alberto','Cánovas')
        self.alumnos.append(alumno1)

    def test_init(self):
        servidor = ServidorDns('192.168.1.254')
        self.assertIsInstance(servidor,ServidorDns)
        self.assertEqual(servidor.direccion_ip,'192.168.1.254')
        self.assertDictEqual(servidor.obtener_registros_tipo_AAA(),[])

    def test_añadir_registro_tipo_AAA(self)-> None:
        servidor = ServidorDns('192.168.1.254')
        nombre_dns = 'www.iesramonarcas.es'
        direccion_ip = '217.160.7.70'
        self.assertDictEqual(servidor.añadir_registro_tipo_AAA(),{'www.iesramonarcas.es':'217.160.7.70'})


    def test_falso(self):
        alumno1 = Alumno(1804140,'Alberto','Cánovas')
        alumno2 = alumno1

        


if __name__ == '__main__':
    unittest.main()