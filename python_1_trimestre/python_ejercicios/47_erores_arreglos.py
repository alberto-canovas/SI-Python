import os
os.system('cls')

hamburgueserias=['McDonals','Foster\'s Hollywood','Burguer King','Popeyes',]

#print(hamburgueserias)
#print(hamburgueserias[2])
#print(hamburgueserias)

#hamburgueserias.remove('Burguer King')
#print(hamburgueserias)

# try:
#     hamburgueserias.remove('Burguer King')
#     print(hamburgueserias)
# except Exception as error:
    #print('Se ha intentado eliminar un elemento qur no existe')

#insertar un elemento si no existe en la lista
def insertar(lista,elemento):
    try:
        posicion=lista.index(elemento)
        
    except Exception as error:
        lista.append(elemento)
        return
    raise Exception (f'No se puede añadir el elemento {elemento} (está ya en la lista, en la posición {posicion})')


insertar(hamburgueserias,'Rohla')
print(hamburgueserias)
try:
    insertar(hamburgueserias,'Burguer King')
    print(hamburgueserias)
except Exception as error:
    
