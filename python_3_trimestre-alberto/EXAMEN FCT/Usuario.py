class Usuario:
    def __init__(self, login: str, contraseña: str, nombre_completo:str) -> None:
        self.__login = login
        #cuando el método es estático ponemos Usuario, si NO lo es ponemos SELF.
        if not Usuario.es_contraseña_compleja(contraseña):
            raise UsuarioError ('La contraseña no cumple los requisitos de complejidad.')

        self.__contraseña = contraseña
        self.__nombre_completo = nombre_completo



    @property
    def login(self):
        return self.__login

    @property
    def nombre_completo(self):
        return self.__nombre_completo
    
    @nombre_completo.setter
    def nombre_completo(self, valor:str) -> None:
        self.__nombre_completo = valor

    #método estático, para indicar que no es estático NO hay que poner el SELF
    def es_contraseña_compleja(contraseña) -> bool:
        if len(contraseña) >=8:
            return True
        else:
            return False
        
    #si es un boleano NO hay que poner EXCEPCIONES

    def supera_autenticacion(self,contraseña) -> bool:
        #si la contraseña que pasan (contraseña) es la misma que la del objeto(self.__contraseña) pasa la autenticación
        if contraseña == self.__contraseña:
            return True
        else:
            return False


class UsuarioError(Exception): ...