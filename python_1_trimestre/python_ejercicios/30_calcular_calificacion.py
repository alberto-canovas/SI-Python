import os
os.system('cls')

#calificaciones=[5,5,5,5,5,5,5,5]
ponderaciones=[0.75,0.75,1.00,1.00,1.25,1.5,2,1.75]

def calcular_nota_examen(ponderaciones,calificaciones):
    calificacion=0
    for i in range(0,len(ponderaciones)):
        # calificacion=calificacion+ponderaciones[i]*calificaciones[i] ES LO MISMO QUE LA SIGUIRNTE LINEA
        calificacion+=ponderaciones[i]*calificaciones[i]
    # calificacion=calificacion/10 ES LO MISMO QUE LA SIGUIENTE LINEA
    calificacion/=10
    return calificacion
# print(calcular_nota_examen(ponderaciones,calificaciones))
# print(calcular_nota_examen(ponderaciones,[10,10,10,10,10,10,10,10]))


def pedir_calificaciones():
    cuantas= int(input('¿Cuántas preguntas tiene el examen? '))
    calificaciones=[]
#range(0,cuantas) ---> del 0 al 7  range(1, cuantas+1)----> del 1 al 8 
    for i in range(1, cuantas+1):
        calificacion=int(input(f'Dime la calificacion de la pregunta {i}: '))
        calificaciones.append(calificacion)
    return calificaciones

calificaciones=pedir_calificaciones()
print(calcular_nota_examen(ponderaciones,calificaciones))


