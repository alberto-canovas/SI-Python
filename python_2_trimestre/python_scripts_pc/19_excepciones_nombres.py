import os
nombres = ['Alicia','Pepe','Laura','Alberto']
apellidos = ['Canovas','Garcia','Martinez','Lopez']


apellidos_error = ['Canovas','Garcia','Martinez']
nombres_error = ['Alicia ','Pepe ','Laura ','Alberto ','Juan']


print(len(nombres))


def juntar_nombres_apellido(nombres,apellidos):
    nombres_y_apelllidos =[]
    if len(nombres) != len(apellidos):
        raise Exception('Las listas no contienen la misma cantidad de datos ')
    for i in range (0,len(nombres)):
        nombres_y_apelllidos.append(f'{nombres[i]} {apellidos[i]}')
    print (nombres_y_apelllidos)



os.system('cls')
try:
    juntar_nombres_apellido(nombres,apellidos)
    
    juntar_nombres_apellido(nombres_error,apellidos)
    
    juntar_nombres_apellido(nombres,apellidos_error)
except Exception as error:
    print(error)

