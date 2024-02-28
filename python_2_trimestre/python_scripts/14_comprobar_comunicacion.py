import subprocess
import sys

def main():
    argumentos=sys.argv[1]
    limpiar_pantalla()
    comprobar_comunicaciones(argumentos)


def comprobar_comunicaciones(argumentos):
    resultado=subprocess.run(['ping','-c','1',argumentos],text=True, capture_output=True)
    if resultado.returncode==0:
        print(f'Existe comunicacion con el equipo {argumentos}')
    if resultado.returncode==1:
        print(f'No existe comunicacion con el equipo {argumentos}')

def limpiar_pantalla():
   subprocess.run('clear')

if __name__ == '__main__':
    main()
