ponderaciones=[0.5, 0.5, 1, 1.5, 2, 1.5, 3]
calificaciones=[10, 10, 10, 10, 10, 10, 5]

canciones=[
    {'interprete':'estopa','titulo':'luna llena','valoracion':6},
    {'interprete':'shakira','titulo':'waka waka','valoracion':8},
    {'interprete':'queen','titulo':'bohemian rapsody','valoracion':10},
    {'interprete':'the beatles','titulo':'yellow submarine','valoracion':3},
]


def calcular_calificacion(calificaciones):
    suma_total=0
    for i in range(0,len(calificaciones)):
        suma_total=(ponderaciones[i]*calificaciones[i])+suma_total
    calificacion=suma_total/10
    return(calificacion)

print(calcular_calificacion(calificaciones))





# def ordenar_por_valoracion(canciones):
#     canciones_ordenadas=[]

#     for j in range(0,len(canciones)):
#         maximo = -1
#         posicion_maximo = -1
#         for i in range(0,len(canciones)):
#             if canciones[i]['valoracion'] > maximo:
#                 maximo=canciones[i]['valoracion']
#                 posicion_maximo=i
#         canciones_ordenadas.append(canciones[posicion_maximo])
#         canciones[posicion_maximo]['valoracion']=-1
#     hola='hola'


# def ordenar_por_valoracion_bis(canciones):

#     for j in range(0,len(canciones)):
#         maximo = -1
#         posicion_maximo = -1

#         for i in range(j,len(canciones)):

#             if canciones[i]['valoracion'] > maximo:
#                 maximo=canciones[i]['valoracion']
#                 posicion_maximo=i

#         cancion_auxiliar=canciones[j]
#         canciones[j]=canciones[posicion_maximo]
#         canciones[posicion_maximo]=cancion_auxiliar


#     hola='hola'
# canciones_ordenadas=ordenar_por_valoracion_bis(canciones)
# print(canciones_ordenadas)
