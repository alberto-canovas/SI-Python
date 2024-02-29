import os
os.system('cls')


base_imponible= 70.5
iva=21.0


def calcular_importe(base_imponible,iva):

    importe=base_imponible +(base_imponible*(iva/100))

    return importe

importe_final= calcular_importe(base_imponible,iva)
print("{:.2f}".format(importe_final))

def calcular_iva(iva):
    impuesto=base_imponible*(iva/100)
    return impuesto

impuesto=calcular_iva(iva)
print("{:.2f}".format(impuesto))

              
         