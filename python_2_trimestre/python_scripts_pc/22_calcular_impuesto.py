import subprocess,sys


impuesto_valor_añadido = [
    {
        "año" : 2024,
        "exento" : 0.0,
        "superreducido" : 4.0,
        "reducido" : 10.0,
        "normal" : 21.0,
    },
    {
        "año" : 2013,
        "exento" : 0.0,
        "superreducido" : 4.0,
        "reducido" : 10.0,
        "normal" : 21.0,
    },
    {
        "año" : 2012,
        "exento" : 0.0,
        "superreducido" : 4.0,
        "reducido" : 8.0,
        "normal" : 18.0
    },
    {
        "año" : 2010,
        "exento" : 0.0,
        "superreducido" : 4.0,
        "reducido" : 7.0,
        "normal" : 16.0,
    },

]

def main():
    argumentos=sys.argv[1:]
    try:
        limpiar_pantalla()
        son_argumentos_correctos(argumentos)
        obtener_base_imponible(argumentos)
        obtener_tipo_impuesto(argumentos)
    except Exception as error:
         print(error)

def son_argumentos_correctos(argumentos):
    base_imponible = argumentos[0]
    tipo_impuesto = argumentos[1]
    num_argumentos = 2

    if len(argumentos)!=num_argumentos:
        raise Exception(f'Debe introducir {num_argumentos} argumentos')
        
    if not base_imponible.isnumeric():
        raise Exception ('El primer argumento debe de ser un número positivo.')

    if not tipo_impuesto ==  'exento' or 'reducido' or 'superreducido' or 'normal':
         raise Exception('El segundo argumento debe de ser (exento), (reducido), (superreducido) o (normal).')


def obtener_base_imponible(argumentos):
    # base_imponible = argumentos[0]
    # if not base_imponible.isnumeric():
    #     raise Exception ('El primer argumento debe de ser un número positivo.')

    print('ok')


def obtener_tipo_impuesto(argumentos):
    # tipo_impuesto = argumentos[1]
    # if not tipo_impuesto ==  'exento' or 'reducido' or 'superreducido' or 'normal':
    #      raise Exception('El segundo argumento debe de ser (exento), (reducido), (superreducido) o (normal).')
    
    print('ok TIPO IMPUESTO')    
    



def limpiar_pantalla():
    subprocess.run('clear')

if __name__ == '__main__':
    main()