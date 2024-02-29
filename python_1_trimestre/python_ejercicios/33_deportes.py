import os
os.system('cls')

#Crea una lista con diez deportes.
deportes=['futbol','basket','waterpolo','tenis','padel',
          'ping-pong','chess','fronton','gym','hockey']
#Intenta cambiar de posición entre ellos los deportes que ocupan las posiciones 2 y 7.


deporte= deportes[2]
deportes[2]= deportes[7]
deportes[7]=deporte
print(deportes)
print(deportes.sort())
print(deportes)
