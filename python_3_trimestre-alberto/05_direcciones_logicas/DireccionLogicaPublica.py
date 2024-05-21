from DireccionLogica import CuatroOctetos
from DireccionLogicaPrivada import DireccionLogicaPrivada


class DireccionLogicaPublica(CuatroOctetos):
    
    def es_formato_correcto(direccion_logica: str) -> bool:
        return not DireccionLogicaPrivada.es_formato_correcto(direccion_logica)