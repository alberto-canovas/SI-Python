import os
os.system('cls')

nombres=[]
edades=[]


# for i in range(0,5):
#     nombre=input('Dime un nombre: ')
#     nombres.append(nombre)
#     edad=int(input('Dime su edad: '))
#     edades.append(edad)

# for i in range(0,5):
#     print(f'La persona {nombres[i]} tiene {edades[i]} años')


personas=[]

for i in range(0,5):
    nombre=input('Dime un nombre: ')
    edad=int(input('Dime su edad: '))
    personas[i][0]=nombre
    personas[i][1]=edad

for persona in personas:
    print(f'La persona {personas[0]} tiene {personas[1]} años')
