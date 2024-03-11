import os, subprocess


def main():
    limpiar_pantalla()
    separar_extension()



def separar_extension():
    resultado=subprocess.run(['ls'],text=True,capture_output=True)
    nombre_archivos= resultado.stdout.strip().split()
    print(f'arcg {nombre_archivos}')
    lista_archivos=[]

    # for i in range(0,len(nombre_archivos)):
    #     archivo=nombre_archivos[i].split('.')
    #     print(f'ok{archivo}')
    #     lista_archivos.append(archivo)

    #    return lista_archivos
    
    for archivo in nombre_archivos:
        print(archivo.split('.'))
        lista_archivos.append(archivo.split('.'))
    print(lista_archivos)

    extension = []
    nombre = []
    sin_extension = []
    extension_3 =[]
    extension_4 = []
    for i in range(0, len(lista_archivos)):
        if len(lista_archivos[i])<=1:
            sin_extension.append(lista_archivos[i][0])
            continue
        elif(len(lista_archivos[i][1]))==3:
            extension_3.append(lista_archivos[i][1])
            continue
        elif(len(lista_archivos[i][1]))==4:
            extension_4.append(lista_archivos[i][1])
        else:
            print(lista_archivos[i][0])
        

        if len(lista_archivos[i])>2:
            extension.append(lista_archivos[i][2])
        else:
            extension.append(lista_archivos[i][1])
            nombre.append(lista_archivos[i][0])
    
    #nombre_y_extension=nombre_archivos[].split('.')
    # extension = []
    # nombre = []

    # for  in range(0,len(lista_archivos)):
    #     extension.append(lista_archivos[1])
    #     nombre.append(lista_archivos[0])
    
    print(f'sin extension {sin_extension}')
    print(f'3 extension {extension_3}')
    print(f'4 extension {extension_4}')
    
    print(f' extension {extension}')
    print(f' nombre {nombre}')




def limpiar_pantalla():
    subprocess.run('clear')



if __name__ == '__main__':
    main()