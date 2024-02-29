import os
os.system('cls')

componentes_Von_Newman=[
    'Procesador',
    'Memoria principal',
    'Memoria secundaria',
    'Dispositivos Entrada/Salida']

print(f'Los elementos que forman la arquitectura Von Newman son:')
# print('\t2',componentes_Von_Newman[1])
# print('\t3',componentes_Von_Newman[2])
# print('\t4',componentes_Von_Newman[3])

i=0
while i < len(componentes_Von_Newman):
    print(f'\t{i+1}) {componentes_Von_Newman[i]}')
    i+=1
