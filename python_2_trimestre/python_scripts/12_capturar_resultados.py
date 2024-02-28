import subprocess

#IMPRIME UN 0 si se ha ejecutado correctamente el comando y un 1 si ha habido un error [.returncode]
#El capture_output borra los errores que aparecen en pantalla en inglés



resultado = subprocess.run(['mkdir','hola'], text=True, capture_output=True)
#print(resultado.returncode) 
if resultado.returncode == 0:
    print('El directorio se ha creado con éxito')
else: 
    print('No se ha podido crear el directorio')

resultado = subprocess.run(['mkdir','hola'], text=True, capture_output=True)
#print(resultado.returncode)
if resultado.returncode == 0:
    print('El directorio se ha creado con éxito')
else: 
    print('No se ha podido crear el directorio')
