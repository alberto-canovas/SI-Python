import os
os.system('cls')

espanyol=['rojo','verde','azul','amarillo','negro','naranja','blanco','marron']
ingles=['red','green','blue','yellow','black','orange','white','brown']
frances=['rouge','vert','bleu','jaune','noir','orange','blanc','marron']
aleman=['rot','grün','blau','gelb','schwarz','orange','weiß','braun']


def traducir_espanyol_ingles(color_espanyol):

    for i in range(0,len(espanyol)):
        if color_espanyol==espanyol[i]:
            return ingles[i]
        
def traducir_espanyol_frances(color_espanyol):

    for i in range(0,len(espanyol)):
        if color_espanyol==espanyol[i]:
            return frances[i]

print(traducir_espanyol_ingles('negro'))




# print('1. Francés')
# print('2. Inglés')
# print('3. Alemán')
# input('Seleccione un idioma (número)')

