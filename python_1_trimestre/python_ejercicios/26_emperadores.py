import os
os.system('cls')

emperadores=['Augusto',
             'Tiberio',
             'Calígula', 
             'Claudio', 
             'Nerón', 
             'Galba', 
             'Otón', 
             'Vitelio',
             'Vespasiano',
             'Tito',
             'Domiciano']

i=0
for i in range(0,len(emperadores)):
    if i==0:
        print(f'{i+1}) {emperadores[i]} fue el primer emperador' )
    elif i==len(emperadores)-1:
        print(f'{i+1}) {emperadores[i]} fue el último emperador')
    else:
        print(f'{i+1}) {emperadores[i]} sucedió a {emperadores[i-1]}')
        i+=1




    
    
