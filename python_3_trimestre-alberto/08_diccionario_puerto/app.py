from enum import Enum
from LibreriaCapaTransporte import Aplicacion


def main():
    puerto_http = PuertoRed(80,TipoServicio.TCP)
    puerto_https = PuertoRed(443,TipoServicio.TCP)
    puerto_mysql = PuertoRed(3306,TipoServicio.TCP)
    puerto_oracle = PuertoRed(1521,TipoServicio.TCP)
    puerto_ftp = PuertoRed(21,TipoServicio.TCP)

    puertos_ocupados: dict[PuertoRed, Aplicacion] = {}
    
    puertos_ocupados[puerto_ftp] = 'Filezilla Server.exe'
    puertos_ocupados[puerto_http] = 'Apache Server.exe'
    puertos_ocupados[puerto_https] = 'Apache Server.exe'
    puertos_ocupados[puerto_mysql] = 'mysqld.exe'
    



    RESTRICCION_PROHIBIDISIMA = 1023
    RESTRICCION_INFERIOR_PROGRAMADORES = 1024
    RESTRICCION_SUPERIOR_PROGRAMADORES = 32767
    RESTRICCION_INFERIOR_WINDOWS = 32768
    RESTRICCION_SUPERIOR_WINDOWS = 65535


    puerto_chrome1 = PuertoRed(80,TipoServicio.TCP)
    puerto_chrome2 = PuertoRed(80,TipoServicio.TCP)
    puerto_firefox = PuertoRed(80,TipoServicio.TCP)
    puerto_chrome3 = PuertoRed(80,TipoServicio.TCP)

    puertos_ocupados[puerto_chrome1] ='chrome.exe' 
    puertos_ocupados[puerto_chrome2] ='chrome.exe' 
    puertos_ocupados[puerto_firefox] ='firefox_browser.exe' 
    puertos_ocupados[puerto_chrome3] ='chrome.exe'

    print('Las conexiones activas son: ')
    for puerto in puertos_ocupados:
        print(puerto.tipo.name, puerto.numero, puertos_ocupados[puerto])
        #print(f'Las conexiones activas son: {puerto}')



    programa = 'chrome_browser.exe'
    puerto_chrome = ...

class TipoServicio(Enum):
    TCP = 'tcp'
    UDP = 'udp'


class PuertoRed:
    PUERTOS_LIMITE_INFERIOR = 0 #propiedad estática
    PUERTOS_LIMITE_SUPERIOR = 65535 #propiedad estática

    def __init__(self,numero: int, tipo: TipoServicio) -> None:
        if not PuertoRed.es_numero_puerto_correcto(numero):
            raise PuertoError(f'El número de puerto {numero} no es posible')
        
        self.__numero = numero
        self.__tipo = tipo

    @property
    def numero(self):
       return self.__numero
    
    @property
    def tipo (self):
        return self.__tipo
    
    @numero.setter
    def numero(self, valor):
        if not PuertoRed.es_numero_puerto_correcto(valor):
            raise PuertoError(f'El número de puerto {valor} no es posible')
        self.__numero = valor
    
    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor

    def es_numero_puerto_correcto(numero:int) -> bool:
        # if numero < Puerto.PUERTOS_LIMITE_INFERIOR or numero > Puerto.PUERTOS_LIMITE_SUPERIOR:
        #     return False
        # else:
        #     return True
        return numero >= PuertoRed.PUERTOS_LIMITE_INFERIOR and numero <= PuertoRed.PUERTOS_LIMITE_SUPERIOR
    
    def obtener_puerto_libre(numero:int):
        if numero >= PuertoRed.PUERTOS_LIMITE_INFERIOR and numero <= PuertoRed.PUERTOS_LIMITE_SUPERIOR:
            return numero
        else: 
            ...

class PuertoError(Exception): ...

if __name__ == '__main__':
    main()