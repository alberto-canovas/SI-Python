import sys,os
from Usuario import Usuario,UsuarioError
from Fichero import Fichero
from ServidorFtp import ServidorFtp

servidor=ServidorFtp(1000)

print('---------- MENÚ PRINCIPAL ----------')
print('1. Iniciar sesión')  
print('2. Ver usuarios registrados')
print('3. Registrar usuario.')
print('4. Salir.')
opcion=input('Introduce una opción: ')

match(opcion):

        case '1':
            login=input('Introduce el login: ')
            password=input('Introduce la contraseña: ')
            name=ServidorFtp.obtener_nombre_completo_usuario(login)

            usuario=Usuario(login,password,name)
            if(ServidorFtp.son_usuario_y_contraseña_validos(login,password)==True):
                print(f'---------- MENÚ {usuario.name} ----------')
                print('1. Mostrar mis ficheros subidos.')
                print('2. Subir fichero.')
                print('3. Mostrar todos los ficheros subidos.')
                print('4. Cerrar sesión.')

                opcion_user=input('Introduce una opcion: ')

                if opcion_user < 0 or opcion_user > 4:
                     raise Exception('Debe introducir una opción entre el 1 y el 4.')
                
                match(opcion_user):
                    case '1':
                        ServidorFtp.obtener_ficheros_almacenados()
                        ServidorFtp.calcular_almacenamiento_ocupado()
                    case '2':
                        ServidorFtp.almacenar_fichero(usuario,)
                    case '3':
                        ServidorFtp.obtener_ficheros_almacenados()
                        ServidorFtp.calcular_almacenamiento_ocupado()
                    case '4':
                        print('Sesión cerrada correctamente')
                        

            

        case '2':
            print('Los usuarios registrados son:')
            for login in ServidorFtp.__usuarios_registrados.keys:
                f'   * {ServidorFtp.obtener_nombre_completo_usuario(login)}'

        case '3':
            login=input('Introduce el login: ')
            password=input('Introduce la contraseña: ')
            name = input('Introduce el nombre completo: ')
            usuario= Usuario(login,password,name)

            ServidorFtp.registrar_usuario(login,usuario)
            
        case '4':
            print('Saliendo...')
            sys.exit()
            