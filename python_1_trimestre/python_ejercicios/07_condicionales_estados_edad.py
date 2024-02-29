import os
# if os.name== 'nt': #New Technologies WINDOWS
#     os.system('cls')
# else: #posix es unix
#     os.system('clear')
os.system('cls' if os.name == 'nt' else 'clear')
edad= 5

if edad<2:
    print('Eres un bebé')
elif edad<12:
    print('Eres un niño')
elif edad<18:
    print('Eres adolescente')
elif edad<35:
    print('Eres un joven')
elif edad<65:
    print('Eres un madurito')
else:
    print('Eres un anciano')
