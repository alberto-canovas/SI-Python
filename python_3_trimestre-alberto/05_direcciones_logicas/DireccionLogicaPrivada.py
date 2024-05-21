from DireccionLogica import CuatroOctetos 


class DireccionLogicaPrivada(CuatroOctetos):

    # def __init__(self, direccion_logica: str) -> None:
    #     super().__init__(direccion_logica)

        #si no aparece la palabra self el método es estático
    def es_formato_correcto(direccion_logica: str) -> bool:
        if not CuatroOctetos.es_formato_correcto(direccion_logica):
            return False

        # if direccion_logica.startswith('10.') or direccion_logica.startswith('192.168.'):
            # return True

        # return True
        

        partes = direccion_logica.split('.')
    
        if partes[0]!='10' and partes[0]!= '172'and partes[0]!='192':
            return False
    
        if partes[0] == '172' and (int(partes[1]) < 16 or int(partes[1]) > 31):
            return False
    
        if partes[0] == '192' and partes[1] != '168':
            return False
    
        return True
       