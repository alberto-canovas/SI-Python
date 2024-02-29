import os
os.system('cls')

clientes_gimnasio = [
    ['Juan', 'M', 182, 92],
    ['Alicia', 'F', 157, 52],
    ['Manuel', 'M', 171, 75],    
]

#Añade manualmente a esa lista cuatro clientes más.

clientes_gimnasio.append(['Loli', 'F', 160, 60])
clientes_gimnasio.append(['Pepe', 'M', 194, 70])
clientes_gimnasio.append(['Paco', 'M', 178, 79])
clientes_gimnasio.append(['Manolo', 'M', 175, 80])

print(len(clientes_gimnasio))

#Crea una variable llamada cliente_ocho y almacena la descripción en forma de lista del cliente. 
# Añádelo a la otra lista con append.

cliente_ocho=['María','F',150,50]

clientes_gimnasio.append(cliente_ocho)
print(len(clientes_gimnasio))

#Crea una variable llamada cliente_nueve inicializada como lista vacía. 
# Accediendo paso a paso, en la posición 0 pon el nombre, en la posición 1 pon el género, en la posición 2 pon la estatura y en la posición 3 pon la masa. 
# (NO se si va a permitir hacer esto). Añádelo con append.

cliente_nueve=[]
# cliente_nueve[0]='Pedro'
# cliente_nueve[1]='M'
# cliente_nueve[2]=185
# cliente_nueve[3]=100
# cliente_nueve.append(cliente_nueve[3],cliente_nueve[2],cliente_nueve[1],cliente_nueve[0])

cliente_nueve.insert(0,'Pedro')
cliente_nueve.insert(1,'M')
cliente_nueve.insert(2,'185')
cliente_nueve.insert(3,'100')
print(cliente_nueve)

#Crea una variable llamada cliente_diez inicializada como lista vacía. 
# Solicita por teclado la información y añádela. Finalmente añade el cliente al final de la lista.

cliente_diez=[]

cliente_diez_nombre=input('Dime un nombre: ')
cliente_diez.append(cliente_diez_nombre)

cliente_diez_genero=input('Dime un género: ')
cliente_diez.append(cliente_diez_genero)

cliente_diez_cm=int(input('Dime una altura (en cm): '))
cliente_diez.append(cliente_diez_cm)

cliente_diez_kg=int(input('Dime un peso (en kg): '))
cliente_diez.append(cliente_diez_kg)

print(cliente_diez)
clientes_gimnasio.append(cliente_diez)
print(clientes_gimnasio)







