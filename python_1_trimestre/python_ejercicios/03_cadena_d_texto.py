print('\n\n')

texto1= "Hola"
texto2= "Pepe"
texto3= "Python"

#Primera forma de concatenar
print("Mi mensaje es: " +texto1+ ", soy "+texto2+ ". Me gusta "+texto3+".")

# Segunda forma: f-string

lenguaje = 'Python'
calificacion= 10

print(lenguaje +  str(calificacion))
print(f'Mi mensaje es: {lenguaje} se merece un {calificacion}.')

#Tercera forma

print('Mi mensaje es: %s se merece un %d'% (lenguaje, calificacion))

#stack overflow pagina para buscar cosas relacionadas con la programación

#Cuarta forma

print('Mi mensaje es: {0} se merece un {1}'.format (lenguaje,calificacion))