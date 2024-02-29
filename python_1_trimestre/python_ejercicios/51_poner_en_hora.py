import os
os.system('cls')


reloj_1={
    'hora':0,
    'minutos':0,
    'segundos':0
}

reloj_2={
    'hora':0,
    'minutos':0,
    'segundos':0
}


def poner_en_hora(reloj,hora,minutos,segundos):

    if hora < 0 or hora > 23:
        raise Exception(f'El valor {hora} es incorrecto para la hora.')
    elif minutos < 0 or minutos > 59:
        raise Exception(f'El valor {minutos} es incorrecto para los minutos.')
    elif segundos < 0 or segundos > 59:
        raise Exception(f'El valor {segundos} es incorrecto para los segundos.')
    else:
        reloj['hora']=hora
        reloj['minutos']=minutos
        reloj['segundos']=segundos

def pedir_valores():
    hora=int(input('Dime la hora: '))
    minutos=int(input('Dime los minutos: '))
    segundos=int(input('Dime los segundos: '))
    
    return (hora,minutos,segundos)

try:
    valores=pedir_valores()
    poner_en_hora(reloj_1,valores[0],valores[1],valores[2])
    print(reloj_1)
except Exception as error:
    print(f'ERROR: {error}')

try:
    valores=pedir_valores()
    poner_en_hora(reloj_2,valores[0],valores[1],valores[2])
    print(reloj_2)
except Exception as error:
    print(f'ERROR:{error}')
