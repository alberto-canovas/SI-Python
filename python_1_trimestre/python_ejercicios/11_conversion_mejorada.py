import os
os.system('cls')
#la funcion tiene que empezar por verbo en infinitivo, que describa la tarea que realiza
def pasar_decimal_a_binario(decimal): #tenemos que poner (decimal) porque es la variable que vamos a cambiar a binario
    
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

    return binario

decimal=int(input('Dime un número decimal: '))
binario= pasar_decimal_a_binario(decimal)
print (binario)

#pasar_decimal_a_binario(254)
