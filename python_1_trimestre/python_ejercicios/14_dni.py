import os
os.system ('cls')

def comprobar_dni(numero,letra):
    resto=numero%23
    if resto==0:
        if letra=='T':
            return True
        else:
            return
        