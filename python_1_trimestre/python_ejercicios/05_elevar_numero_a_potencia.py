import os #operating system/sistema operativo
os.system('cls')

print('\n')

base=2
exponente=10

#Primera forma

resultado=base**exponente
print(f'El número {base} elevado a {exponente} es {resultado}.')
print(f'El número \'{base}\' elevado a \'{exponente}\' es \'{resultado}\'.')
print(f'El número "{base}" elevado a "{exponente}" es "{resultado}".')

#Segunda forma
base=5
exponente=2
resultado=pow(base,exponente)
print(f'El número {base} elevado a {exponente} es {resultado}.')

#Tercera forma
import math
resultado= math.pow(base,exponente)
print(f'El número {base} elevado a {exponente} es {resultado:.0f}.')