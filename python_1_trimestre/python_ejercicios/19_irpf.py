import os
os.system('cls')

def calcular_porcentaje_total_irpf_(sueldo_bruto,porcentaje_total):
    if sueldo_bruto<=12450:
        porcentaje_total==19/100

    elif sueldo_bruto<=20199:
        porcentaje_total==24/100

    elif sueldo_bruto<=35199:
        porcentaje_total==30/100

    elif sueldo_bruto<=59999:
        porcentaje_total==37/100

    elif sueldo_bruto<=299999:
        porcentaje_total==45/100
    
    elif sueldo_bruto>=300000:
        porcentaje_total==47/100



