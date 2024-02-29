import os
os.system('cls')

temperaturas=[35,
    35,
    34,
    29,
    31,
    31,
    31,
    30,
    30,
    35,
    31,
    31,
    30,
    31,
    31,
    31,
    33,
    34,
    31,
    31,
    31,
    32,
    33,
    33,
    35,
    36,
    33,
    31,
    32,
    29,
    30]


def calcular_temperatura_media(temperaturas):
    sumatotal=0
    for temperatura in temperaturas:
        sumatotal+=temperatura

    media=sumatotal/len(temperaturas)
    return round(media,2) 


print(calcular_temperatura_media(temperaturas))

def calcular_temperatura_maxima(temperaturas):
    maximo=temperaturas[0]
    for temperatura in temperaturas:
        if temperatura> maximo:
            maximo=temperatura
    return maximo

print(calcular_temperatura_maxima(temperaturas))


def calcular_temperatura_minima(temperaturas):
    minimo=temperaturas[0]
    for temperatura in temperaturas:
        if temperatura < minimo:
            minimo=temperatura
    return minimo

print(calcular_temperatura_minima(temperaturas))







