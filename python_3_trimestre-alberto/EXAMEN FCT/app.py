
def main():
    mostrar_menu_principal()



def mostrar_menu_principal():
    while True:
        print('------------ MENÚ PRINCIPAL -------------')
        print('1. Iniciar sesión.')
        print('2. Ver usuarios registrados.')
        print('3. Registrar usuario.')
        print('4. Salir.')

        opcion = input('Introduce una opcion: ')
        match opcion:
            case '1':
                iniciar_sesion()
            case '2':
                ver_usuarios_registrados()
            case '3':
                registrar_usuario()
            case '4':
                break



def iniciar_sesion():...


def ver_usuarios_registrados(): ...


def registrar_usuario(): ...





def mostrar_menu_servidor():
    ...



if __name__ == '__main__':
    main()