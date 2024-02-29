import os
os.system('cls')

modulos=['entornos de desarrollo','programación','fol','inglés','sisemas informáticos','bases de datos','empresa']

# i=0
# while i<len(modulos):
#     print(f'{i+1}) {modulos [i]}')
#     i+=1


# i=1
# for modulo in modulos:
#     print(f'{i}) {modulo}')
#     i+=1


i=0
for i in range(0,len(modulos)):
    print(f'{i+1}) {modulos [i]}')


for i, modulo in enumerate(modulos):
    print(f'{i+1}) {modulos [i]}')

    