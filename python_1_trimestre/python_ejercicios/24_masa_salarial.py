import os
os.system('cls')

salarios=[1500,1250,2300,900,900,2800,1600,1500,1800]
# masa_salarial_cutre=salarios[0]+salarios[1]+salarios[2]+salarios[3]+salarios[4]+salarios[5]+salarios[6]+salarios[7]+salarios[8]
# print(f'Hay {len(salarios)} empleados y la masa salarial es {masa_salarial_cutre}')


masa_salarial=0
for i in range(0,len(salarios)):
    masa_salarial=masa_salarial+salarios[i]
    
print(f'Hay {len(salarios)} empleados y la masa salarial es {masa_salarial}')


masa_salarial=0
for salario in salarios:
    masa_salarial+=salario
print(f'Hay {len(salarios)} empleados y la masa salarial es {masa_salarial}')
