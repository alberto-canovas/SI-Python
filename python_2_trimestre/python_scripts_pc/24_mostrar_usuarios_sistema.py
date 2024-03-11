import subprocess, os


def main():
    try:
        limpiar_pantalla()
        usuarios = obtener_usuarios() #ok
        usuarios_ordenados = ordenar_usuarios(usuarios) #ok
        #mostrar_usuarios(usuarios) #ok
        fecha = mostrar_fecha() #ok
        numero_usuarios=mostrar_numero_usuarios(usuarios) #ok
        print(f'En la fecha {fecha} hay {numero_usuarios} usuarios en el sistema y son: {usuarios_ordenados}.')

    except Exception as error:
        print(error)



def limpiar_pantalla():
    subprocess.run('clear')

def mostrar_numero_usuarios(usuarios):
   print(len(usuarios))
   return len(usuarios)
        

def obtener_usuarios():
    resultado=subprocess.run(['cat','/etc/passwd'],capture_output=True,text=True)
    if resultado.returncode != 0:
        raise Exception('Hay un problema al ejecutar el comando cat.')

    lineas = resultado.stdout.strip().split('\n')
    
    lista_usuarios=[]

    for linea in lineas :
        #print(linea)
        usuario=linea.split(':')
        lista_usuarios.append(usuario[0])

    return lista_usuarios


def mostrar_usuarios(usuarios):
        print(usuarios)

def mostrar_fecha():
    resultado = subprocess.run(['date','+%d/%m/%Y'], capture_output=True, text=True)
    if resultado.returncode !=0:
        raise Exception('Hay un problema con el comando date.')
    fecha = resultado.stdout.strip()
    return fecha

def ordenar_usuarios(usuarios):
    return sorted(usuarios)
    



if __name__ == '__main__':
    main()