import os
os.system('cls')

#cada pregunta se valora entre 0 y 10
pregunta_1=5

pregunta_2=8

pregunta_3=10

pregunta_4=5

#preguntas=pregunta_1+pregunta_2+pregunta_3+pregunta_4
#ponderaciones=ponderacion_1+ponderacion_2+ponderacion_3+ponderacion_4

def calcular_nota(pr1, pr2, pr3, pr4):
    ponderacion_1=3
    ponderacion_2=1
    ponderacion_3=2
    ponderacion_4=4
    # ejercicio1=(pregunta_1*ponderacion_1)/10
    # ejercicio2=(pregunta_2*ponderacion_2)/10
    # ejercicio3=(pregunta_3*ponderacion_3)/10
    # ejercicio4=(pregunta_4*ponderacion_4)/10
    # nota=ejercicio1+ejercicio2+ejercicio3+ejercicio4
    nota=(pr1*ponderacion_1)/10+(pr2*ponderacion_2)/10+(pr3*ponderacion_3)/10+(pr4*ponderacion_4)/10

    return nota

calificación=calcular_nota(10, 10, 10, 10)
print(f'La calificación es {calificación}/10')
calificación=calcular_nota(0, 10, 0, 10)
print(f'La calificación es {calificación}/10')




