import os
os.system('cls')
alumnos=[
    'Marta',
    'Pablo',
    'Dounia',
    'David',
    'Alejandro',
    'Alberto',
    'Abel',
    'Ramón',
    'Antonio',
    'Carlota',
    'Miriam',
    'Angela',
    'Ruben',
    'Jose'
]

print('Los alumnos de la clase son: ')

# i=0
# while i<len(alumnos):
#     print(f'\t{i+1}) {alumnos[i]}')
#     i+=1

# for (i=0; i<len(alumnos);i+=1):  NO EXISTE ESTA SINTAXIS EN PYTHON

# METODO FOR
# i=1
# for alumno in alumnos: #foreach
#     print(f'\t{i}) {alumno}')
#     i+=1

print(list(range(5,30,3)))

for i in range(0,len(alumnos)):
    print(f'\t{i+1}) {alumnos[i]}')

# for i, alumno in enumerate(alumnos):
#     print(f'\t{i+1}) {alumno}')
    