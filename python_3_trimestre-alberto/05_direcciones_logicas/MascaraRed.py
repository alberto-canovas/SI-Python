from CuatroOctetos import CuatroOctetos


class MascaraRed(CuatroOctetos):

    def __init__(self,octetos:str) -> None:
        if not MascaraRed.es_mascara_correcta(mascara):
            raise MascaraRedError


    def es_mascara_correcta(mascara:str) -> bool:
        if mascara in ("255.0.0.0","255.255.0.0","255.255.255.0"):
            return True
        else:
            return False
        

class MascaraRedError(Exception):...
        
