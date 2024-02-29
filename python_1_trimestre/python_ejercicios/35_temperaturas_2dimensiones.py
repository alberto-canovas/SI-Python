import os
os.system('cls')

temperaturas_agosto=[
#numero,dia,tempmin,tempmax
    [1,'M',23,35],
    [2,'X',25,35], 
    [3,'J',24,34],
    [4,'V',23,29],
    [5,'S',20,31]
]

dia_uno=temperaturas_agosto[0]
dia_dos=temperaturas_agosto[1]
dia_tres=temperaturas_agosto[2]
dia_cuatro=temperaturas_agosto[3]
# print(dia_uno)
# print(dia_uno[1])
# print(temperaturas_agosto[3][1])

for dato_diario in temperaturas_agosto:
    #print(dato_diario[1])
    for subdato in dato_diario:
        print(subdato, end=' - ')
    print()