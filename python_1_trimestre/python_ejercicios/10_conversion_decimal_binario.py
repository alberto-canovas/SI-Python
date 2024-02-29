import os
os.system('cls')

#PROGRAMA QUE PIDA UN NUMERO EXPRESADO EN DECIMAL Y LO CONVIERTA A BINARIO

decimal=int(input('Dime un número decimal: '))
binario=''

while True:
    cociente=decimal//2 #división entera
    resto=decimal % 2 #resto de la división
    decimal=cociente

    if cociente<2:
        binario=str(cociente)+str(resto)+binario
        break
    else:
        binario=str(resto)+binario
        continue


print (f'El número {decimal} en binario es {binario}')