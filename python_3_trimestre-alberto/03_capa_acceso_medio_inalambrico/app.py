import os
from PuntoAcceso import PuntoAcceso, PuntoAccesoError
from OrdenadorPortatil import OrdenadorPortatil
from Smartphone import Smartphone
from Tableta import Tableta

os.system('cls')
punto_acceso = PuntoAcceso('wifi_ññ','1234')

portatil1 = OrdenadorPortatil('Asus500','A1:A2:A3:A4:A5:A6')
portatil2 = OrdenadorPortatil('Lenovo500','A0:A2:A3:A4:A5:A6')
movil = Smartphone('Xiaomi P14','A3:A2:A3:A4:A5:A6')
tableta = Tableta('Samsung','A4:A2:A3:A4:A5:A6')

print(portatil1)
print(portatil2)
print(movil)
print(tableta)

print(punto_acceso.equipos_conectados)
portatil1.conectar_wifi(punto_acceso,'1234')
print(punto_acceso.equipos_conectados)

try:
    portatil1.conectar_wifi(punto_acceso,'1234')
    print(punto_acceso.equipos_conectados)
except PuntoAccesoError as error:
    print(error)