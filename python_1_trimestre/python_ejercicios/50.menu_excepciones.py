import os, sys
os.system('cls')


contactos=[
    
]


def crear_contacto():
    nombre= input('Dime un nombre: ')
    apellidos= input('Dime tus apellidos: ')
    edad=pedir_edad()
    telefono=pedir_telefono()

    nuevo_contacto={
        'nombre': nombre,
        'apellidos': apellidos,
        'edad': edad,
        'telefono': telefono
    }

    for contacto in contactos:
        if contacto['telefono']==nuevo_contacto['telefono']:
            #print('Ya existe un usuario con ese teléfono.')
            raise Exception('Ya existe un usuario con ese teléfono.')

    contactos.append(nuevo_contacto)

def pedir_telefono():
    while True:
        try:
            telefono=int(input('Dime tu teléfono: '))
            if telefono <600000000 or telefono>999999999:
                print('El teléfono introducido no es correcto.')
                continue
            break
        except Exception as error:
            print('El teléfono introducido no es correcto.')
            continue
    return telefono

def pedir_edad():
    while True:
        try:
            edad = int(input('Dime tu edad: '))
            if edad < 0 or edad >120:
                print('La edad introducida no es correcta')
                continue
            break
        except Exception as error:
            print('No has introducido un número para la edad.\n')
            continue #sigue entrando en el bucle y pide otra vez la edad hasta que introduzca una correcta
    return edad

    

def mostrar_menu():
    while True:
        print('             MENÚ DE USUARIO')
        print('---------------------------------------------')
        print('1. Pedir datos personales.')
        print('2. Opcion.')
        print('3. Opcion.')
        print('4. Opcion.')
        print('5. Opcion.')
        print('6. Salir de la aplicación.')
        print('')

        opcion=input('Introduce una opcion: ')

        match opcion:
            case '1':
                crear_contacto()
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                sys.exit()
            case _:
                print('Introduce una opcion correcta')

mostrar_menu()



