import os
os.system('cls')

lenguajes=['Java','Python','SQL','CSS','PHP','HTML','JavaScript','SQL','Python']
lenguaje_actual= lenguajes[1] #se empieza a numerar desde el 0
print(f'El lenguaje que estoy estudiando hoy es {lenguaje_actual}.')
print(f'El lenguaje que estoy estudiando con Cuello es {lenguajes[0]}.')
print(f'El longitud o tamaño del array es {len(lenguajes)}.')

print('\nEste tipo de array en Python se denomina lista.')
print(lenguajes)
print(lenguajes.index('SQL')) #devuelve la primera vez que aparece en el array(si hay dos CSS solo devuelve el primero)
print(lenguajes.index('SQL',3)) #empieza a buscar desde la podicion 3 del array(por defecto es 0)




