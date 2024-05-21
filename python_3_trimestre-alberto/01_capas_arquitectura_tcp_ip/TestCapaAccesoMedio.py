import unittest
from Capa1AccesoMedio import Capa1AccesoMedio, TipoMedio, TipoTecnologia

#(unittest.{nombre del objeto padre}) es lo mismo que extends en JAVA

class TestCapaAccesoMedio(unittest.TestCase):
    
    def test_getter_medio(self):
        capa = Capa1AccesoMedio(TipoMedio.INALAMBRICO, TipoTecnologia.BLUETOOTH)
        self.assertEqual(capa.medio, TipoMedio.INALAMBRICO)

    def test_getter_tecnologia(self):
        capa = Capa1AccesoMedio(TipoMedio.INALAMBRICO, TipoTecnologia.BLUETOOTH)
        self.assertEqual(capa.tecnologia, TipoTecnologia.BLUETOOTH)

    def test_setter_medio(self):
        capa = Capa1AccesoMedio(TipoMedio.INALAMBRICO, TipoTecnologia.BLUETOOTH)
        capa.medio = TipoMedio.ALAMBRICO
        self.assertEqual(capa.medio, TipoMedio.ALAMBRICO)

    def test_setter_tecnologia(self):
        capa = Capa1AccesoMedio(TipoMedio.INALAMBRICO, TipoTecnologia.BLUETOOTH)
        capa.tecnologia = TipoTecnologia.COAXIAL
        self.assertEqual(capa.tecnologia, TipoTecnologia.COAXIAL)


if __name__ == '__main__':
    unittest.main()






















