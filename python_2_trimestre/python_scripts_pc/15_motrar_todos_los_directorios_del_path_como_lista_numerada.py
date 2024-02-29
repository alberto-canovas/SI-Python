import subprocess,os






def main():
    limpiar_pantalla()
    mostar_path_como_lista()
    print()
    mostar_path_como_lista_1()

def mostar_path_como_lista():
    resultado = subprocess.run(['echo',os.environ['PATH']],capture_output=True,text=True) 
    #['echo',os.environ['PATH']] hace referencia a escribir en el terminal $PATH
    if resultado.returncode == 0:
        texto = resultado.stdout.strip() #stdout almacena lo que sale en pantalla
        for i in range(0,7):
            print(f'{i+1}){texto.split(':')[i]}')
    else:
        print('No se puede mostrar el PATH.')


#OTRA FORMA DE HACERLO
        
def mostar_path_como_lista_1():
    resultado = subprocess.run(['echo',os.environ['PATH']],capture_output=True,text=True) 
    #['echo',os.environ['PATH']] hace referencia a escribir en el terminal $PATH
    if resultado.returncode == 0:
        linea = resultado.stdout.strip() #stdout almacena lo que sale en pantalla y el strip sirve para quitar el espacio que se queda al final
        linea_troceada = linea.split(':')
        i=1
        for directorio in linea_troceada:
            print(f'{i}){directorio}')
            i+=1
    else:
        print('No se puede mostrar el PATH.')


def limpiar_pantalla():
    subprocess.run('clear')
    

if __name__ == '__main__':
    main()