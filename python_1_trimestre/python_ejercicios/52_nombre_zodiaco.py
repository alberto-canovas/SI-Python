import os
os.system('cls')


persona_1={
    'nombre':None,
    'signo':None
}


persona_2={
    'nombre':None,
    'signo':None
}

SIGNOS_ZODIACO=['Aries', 'Tauro', 'Géminis', 'Cáncer', 'Leo', 'Virgo', 'Libra', 'Escorpio', 'Sagitario', 'Capricornio', 'Acuario',  'Piscis']


def pedir_nombre_y_signo(persona):
    nombre=input('Dime un nombre: ').capitalize()
    signo=input('Dime un signo: ').capitalize()

    if signo not in signos:
        raise Exception(f'El signo del zodiaco {signo} no existe.')
    else:
        persona['signo']=signo
        persona['nombre']=nombre
    return(nombre,signo)

def pedir_nombre_y_zodiaco_bucle(persona):
    nombre=input('Dime un nombre: ').capitalize()
    signo=input('Dime un signo: ').capitalize()

    for signo_indv in SIGNOS_ZODIACO:
        if signo==signo_indv:
            signo_indv=persona['signo']
    return(nombre,signo)

#print(pedir_nombre_y_signo(persona_1))

print(pedir_nombre_y_zodiaco_bucle(persona_1))

# try:
#     pedir_nombre_y_zodiaco_bucle(persona_1)
#     print(persona_1)
# except Exception as error:
#     print(f'ERROR {error}')



# try:
#     pedir_nombre_y_signo(persona_1)
#     print(persona_1)
# except Exception as error:
#     print(f'ERROR {error}')

