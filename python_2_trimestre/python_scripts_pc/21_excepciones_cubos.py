cubo_uno = {
    "capacidad":5,
    "contenido":0
}

cubo_dos = {
    "capacidad":3,
    "contenido":0
}

cubo_tres = {
    "capacidad":2,
    "contenido":0
}

def llenar_cubo(cubo):
    if cubo["contenido"]==cubo["capacidad"]:
        raise Exception('El cubo ya está lleno')
    cubo["contenido"]=cubo["capacidad"]
    print(cubo)

def vaciar_cubo_en_otro(cubo_a_vaciar,cubo_a_llenar):
    
    if cubo_a_vaciar["contenido"]> cubo_a_llenar["capacidad"] - cubo_a_llenar["contenido"]:
        raise Exception ('El cubo a llenar no tiene capacidad.')

    if cubo_a_llenar["contenido"] > cubo_a_llenar["capacidad"] :
        raise Exception('El cubo ha excedido su capacidad.')

    if cubo_a_llenar["contenido"] + cubo_a_vaciar["contenido"] > cubo_a_llenar["capacidad"]:
        raise Exception ('El cubo a llenar no se puede llenar más.')
    


    cubo_a_llenar["contenido"]+=cubo_a_vaciar["contenido"]
    cubo_a_vaciar["contenido"]=0

    print(f'El cubo a llenar tiene {cubo_a_llenar}')
    print(f'El cubo a vaciar tiene {cubo_a_vaciar}')
    print('--------------------------------------')


try:
    
    llenar_cubo(cubo_tres)
    #llenar_cubo(cubo_tres)
    vaciar_cubo_en_otro(cubo_tres,cubo_uno)
    llenar_cubo(cubo_tres)
    vaciar_cubo_en_otro(cubo_tres,cubo_uno)
    llenar_cubo(cubo_tres)
    vaciar_cubo_en_otro(cubo_tres,cubo_uno)

    print(cubo_uno)

except Exception as error:
    print(error)

