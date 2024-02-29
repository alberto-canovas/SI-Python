import os
os.system('cls')


#PRIMER HIJO 200
#SEGUNDO HIJO 250
#TERCER HIJO EN ADELANTE 300


def calcular_degravacion(hijo):
    
    if hijo==1:
        desgrava=200
    elif hijo==2:
        desgrava=250+200
    elif hijo>2:
        desgrava=450
        desgrava=desgrava+300*(hijo-2)
    else:
        desgrava=0
    
    return desgrava


hijo=int(input('¿Cuantos hijos tienes?'))

desgrava=calcular_degravacion(hijo)
print(desgrava)
print(f'Tienes {hijo} hijos y te desgravas {desgrava} euros.')




