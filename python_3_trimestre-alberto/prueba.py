class Vivienda:
    def __init__(self,
            referencia_catastral: str,
            direccion: str,
            superficie: int,
            ciudad: str
            ) -> None:
            self.referencia_catastral = referencia_catastral
            self.direccion = direccion
            self.superficie = superficie
            self.ciudad = ciudad
        
    def __repr__(self) -> str:
        return f'{self.direccion}'

if __name__ == '__main__':
    vivienda1 = Vivienda('123456789ASDFG','Calle san fernando nº3',120,'Totana') 
    vivienda2 = Vivienda('123456789ASDFJ','Calle san Fermín nº7',80,'Totana') 
    vivienda3 = Vivienda('123456789ASDFH','Avenida de los Pacos nº89',190,'Totana') 


    viviendas: dict[str, Vivienda] = {}
    viviendas['123456789ASDFG'] = vivienda1
    viviendas['123456789ASDFJ'] = vivienda2
    viviendas['123456789ASDFH'] = vivienda3

    print(viviendas['123456789ASDFG'])

    #si ponemos una ref catastral que no existe despues del get nos da como valor none
    #print(viviendas.get('123456789ASDF'))

    #si ponemos una ref catastral que no existe con dentro de los [] nos da una excepción KeyError
    #print(viviendas['123456789ASDF'])
    numero_inicio=101
    contador = f'192.168.1.{numero_inicio}'

    print(contador)
    
    print(list(viviendas.keys()))
    print(viviendas.keys())
    viviendas.pop 