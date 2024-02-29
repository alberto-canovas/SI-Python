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
        obtener_base_imponible(argumentos)
        obtener_tipo_impuesto(argumentos)
    except Exception as error:
         print(error)


def obtener_base_imponible(argumentos):
    if not argumentos[0].isnumeric():
        raise Exception ('El primer argumento debe de ser un número positivo.')
    print('ok')


def obtener_tipo_impuesto(argumentos):
    if not argumentos[1] ==  'exento' or 'reducido' or 'superreducido' or 'normal':
         raise Exception('El segundo argumento debe de ser (exento), (reducido), (superreducido) o (normal).')
    print('ok TIPO IMPUESTO')    
    



def calcular_importe_impuesto_aplicado_producto(base_imponible,tipo_argumento,fecha_adquirido):
    ...

for i in range(1,4):
        print(impuesto_valor_añadido[i])

def limpiar_pantalla():
    subprocess.run('clear')

if __name__ == '__main__':
    main()