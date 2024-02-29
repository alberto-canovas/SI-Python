import os
os.system('cls')

dni=input('Dime tu DNI:')
nombre=input('Dime tu nombre: ')
estatura=int(input('Dime tu estatura: '))
peso=int(input('Dime tu peso: '))

datos_personales={}
datos_personales[dni]=dni
datos_personales[nombre]=nombre
datos_personales[estatura]=estatura
datos_personales[peso]=peso

print(datos_personales)

