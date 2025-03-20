
class GeneradorEmail:
    def __init__(self,nombre:str,empresa:str,opc:int):
        self.__nombre:str  = nombre
        self.__empresa:str = empresa
        self.__opc_dominio:int = opc
        self.__dominios = ('.com','.net','.mx')
        
    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def empresa(self) -> str:
        return self.__empresa
        
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de caracteres")
        self.__nombre = nombre

    @empresa.setter
    def empresa(self, empresa: str) -> None:
        if not isinstance(empresa,str):
            raise ValueError("La empresa debe ser cadena de caracteres")
        self.__empresa = empresa
    @property
    def opc_dominio(self) -> int:
        return self.__opc_dominio

    @opc_dominio.setter
    def opc_dominio(self, opc: int) -> None:
        if not isinstance(opc, int):
            raise ValueError("La opción de dominio debe ser un número entero")
        if opc < 0 or opc >= len(self.__dominios):
            raise ValueError("La opción de dominio debe ser mayor o igual a 0 y menor que 3")
        self.__opc_dominio = opc
        
    def generar(self) -> None:
        __nombre = self.__nombre.replace(' ','').lower()
        __empresa = self.__empresa.replace(' ','').lower()
        __dominio = self.__dominios[self.__opc_dominio]
        __email:str = f'{__nombre}@{__empresa}{__dominio}'
        print(__email)

if __name__ == '__main__':
    nombre:str = input('ingresa nombre completo: ')
    empresa:str = input('ingresa tu empresa: ')
    opc:int = int(input('opc: ( 0: .com) (1: .net) (2: .mx): '))
    nueva_emial:object = GeneradorEmail(nombre=nombre, empresa=empresa, opc=opc)
    nueva_emial.generar()
    