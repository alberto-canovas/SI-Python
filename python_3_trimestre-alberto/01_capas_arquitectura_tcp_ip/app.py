import os
from Red import Red
from Capa1AccesoMedio import Capa1AccesoMedio,TipoMedio,TipoTecnologia
from Capa2Interred import Capa2Interred
from Capa3Transporte import Capa3Transporte
from Capa4Aplicacion import Capa4Aplicacion

def main():
    os.system('cls')

    capaAccesoMedio = Capa1AccesoMedio(TipoMedio.INALAMBRICO,TipoTecnologia.WIFI)
    print(capaAccesoMedio)
    print(capaAccesoMedio.medio)
    print(capaAccesoMedio.tecnologia)

    capaAccesoMedio.medio = TipoMedio.ALAMBRICO
    print(capaAccesoMedio.medio)
    capaAccesoMedio.tecnologia = TipoTecnologia.BLUETOOTH
    print(capaAccesoMedio.tecnologia)


    capaInterred = Capa2Interred()
    capaTransporte = Capa3Transporte()
    capaAplicacion = Capa4Aplicacion()
    
    red = Red(capaAccesoMedio, capaInterred, capaTransporte, capaAplicacion)


if __name__ == '__main__':
    main()