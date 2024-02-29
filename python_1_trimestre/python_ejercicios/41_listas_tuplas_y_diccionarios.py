import os
os.system('cls')

#LISTAS: son MUTABLES
marcas_coches=['Seat','Mercedes','Renault','Fiat','Volkswagen','Citroen','Tesla','Ford','Ferrari']
marcas_coches.append('Porsche') #añade una nueva marca a la lista al final
marcas_coches.append('Audi')

#TUPLAS no son mutables, son algo propio de Python. MUTABLE, que se puede alterar, añadir nuevos elementos.

marcas_coches_como_tupla=('Seat','Mercedes','Renault','Fiat','Volkswagen','Citroen','Tesla','Ford','Ferrari')

#DICCIONARIOS: son MUTABLES, se llama en otros lenguajes arrays asociativos. Tienen clave y valor

marcas_coches_como_diccionario={
    'se':'Seat',
    'me':'Mercedes',
    're':'Renault',
    'fi':'Fiat',
    'vo':'Volkswagen',
    'ci':'Citroen',
    'te':'Tesla',
    'fo':'Ford',
    'fe':'Ferrari'
    }

#se accede por clave
el_volkswagen=marcas_coches_como_diccionario['vo']
print(el_volkswagen)

for i in marcas_coches_como_diccionario:
    print(f'El vehículo con clave {i} es {marcas_coches_como_diccionario[i]}')



print()
paises={
    'cam':'Camerun',
    'por':'Portugal',
    'bra':'Brasil',
    'per':'Peru',
    'isl':'Islandia',
    'can':'Canada'
    }
for i in paises:
    print(f'El país con clave {i} es {paises[i]}')

print()
modulos_primero={
    'sis':'Sistemas Informaticos',
    'pro':'Programacion',
    'ing': 'Inglés',
    'bas':'Base de datos',
    'ent':'Entornos de desarrollo',
    'fol':'Formaccion y orientacion laboral',
    'emp':'Empresa'
}
print(f'Los modulos de primero son: ')
for i in modulos_primero:
   print(modulos_primero[i])
