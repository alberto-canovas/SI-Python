import os
os.system('cls')

numeros=[15,1056,10,20,35,376,52,89,100,2520]


# def pasar_decimal_a_otrosistema(decimal):
#     caracteres_hexa=['0123456789ABCDEF']
#     resultado_hex = ''
#     decimal=525
#     while decimal>0:
#         resto=decimal%16
#         resultado_hex=caracteres_hexa[resto]+resultado_hex
#         decimal//=16
#         if resultado_hex=='':
#             resultado_hex='0'
#     return resultado_hex


# resultado_hex=(pasar_decimal_a_otrosistema(decimal))
# print(resultado_hex)

def pasar_decimal_a_otrosistema(base,decimal):

    while True:
            cociente=decimal//base #división entera
            resto=decimal % base #resto de la división
            decimal=cociente

            if cociente<base:
                resultado_hex=obtener_digito_hex(cociente)+obtener_digito_hex(resto)+resultado_hex
                break
            else:
                resultado_hex=obtener_digito_hex(resto)+resultado_hex
                continue
    return resultado_hex


def obtener_digito_hex(digito_decimal):
    if digito_decimal==10:
        return'A'
    elif digito_decimal==11:
        return'B'
    elif digito_decimal==12:
        return'C'
    elif digito_decimal==13:
        return'D'
    elif digito_decimal==14:
        return'E'
    elif digito_decimal==15:
        return'F'     

print(obtener_digito_hex(15))
print(pasar_decimal_a_otrosistema(7843))

def convertir_numeros(numeros):
    hexadecimales=[]
    for numero in numeros:
        hexadecimal=


