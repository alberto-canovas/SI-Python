import os
os.system('cls')

frutas=['melon','sandia','naranja','pera','cereza']
#INTRODUCE AL FINAL DE LA LISTA UNA FRUTA
frutas.append('melocoton')

#BUSCA UNA DETERMINADA FRUTA E IMPRIME SU POSICION
frutas.index('sandia')
print(frutas.index('sandia'))

#Busca una determinada fruta que no exista en la lista e imprime su posición.
# print(frutas.index('mango'))

#En un bucle pide por teclado tres frutas y añádelas a la lista.
# for i in range(0,3):
#     fruta=input('Dime una fruta: ')
#     frutas.append(fruta)

# print(len(frutas))

#En un bucle pide por teclado tres nuevas frutas, es decir, si el usuario intenta añadir una verdura que ya existe que no se le permita y vuelva a intentarlo hasta que se añadan las tres verduras.
frutas_nuevas=0
while frutas_nuevas<3:
    fruta_nueva=input('Dame una fruta: ')
    if frutas.count(fruta_nueva)==0:
        frutas.append(fruta_nueva)
        #frutas_nuevas=frutas_nuevas+1 ES LO MISMO
        frutas_nuevas+=1
    else:
        print('Esa fruta ya existe en la lista')

#otra forma de hacerlo MEJOR
frutas_nuevas=0
while frutas_nuevas<3:
    fruta_nueva=input('Dame una fruta: ')

    if fruta_nueva not in frutas:
        frutas.append(fruta_nueva)
        frutas_nuevas+=1
    else:
        print('Esa fruta ya existe en la lista')


print(len(frutas))

