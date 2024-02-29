import os
os.system('cls')

EURIBOR= 4.078/100 
GANACIA= 0.75/100
interes=4.828/100
prestamo=int(input('¿Cuánto dinero te deja el banco? '))
años=int(input('¿En cuantos años lo devuelves? '))

meses=años*12

def calcular_cuota_mensual(prestamo,meses,interes):
    cuota_mensual=(prestamo/(1-(1/(1+interes))**meses)/interes)/12
    return cuota_mensual


cuota_mensual=calcular_cuota_mensual(prestamo,meses,interes)
print(cuota_mensual)
