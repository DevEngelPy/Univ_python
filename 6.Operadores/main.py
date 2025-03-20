""""
sys de descento vip
la tienda tiene un descuento aquillos que 
compren 10 o mas artuculos y ademas que sean 
miembros de la misma.
el sys solita al cliente cuantos articulos 
va a comprar y si cuenta con membresia.
en caso de a ver comprado 10 pro. y ser miembro
entonces tendra el descuento de vip.
"""
class Vip:
    def __init__(self,art:int,miembro:bool):
        self.__cant_art:int = art
        self.__es_miembro:bool = miembro
    
    @property
    def cant_art(self) -> int:
        return self.__cant_art
    @property
    def es_miembro(self) -> bool:
        return self.__es_miembro
    @cant_art.setter
    def cant_art(self, value: int) -> None:
        self.__cant_art = value

    @es_miembro.setter
    def es_miembro(self, value: bool) -> None:
        self.__es_miembro = value
    
    def __descuento(self) -> str:
        if self.__cant_art >= 10 and self.__es_miembro:
             return 'si hay desciento!'
    
    def __str__(self) -> str:
        return f'Descuento ?: \n - {self.__descuento()}'
#ejemplo de or prestamo de libro
class EjemploOr:
    def __str__(self):
        DISTANCIA_PERMITIDA:int = 3
        credencial:str = input('cuentas con credencial ? (si/no)')
        distancia_km:int = int(input('a cuantos km vives de la biblioteca? '))
        if credencial.strip().lower() == 'si' or distancia_km <= DISTANCIA_PERMITIDA:
            return 'si hay prestamo'
        else:
            return 'no hay prestamo'
if __name__ == '__main__':
    """nuevo_vip:object = Vip(10,True)
    print(nuevo_vip)
    """
    ejm:object = EjemploOr()
    print(ejm)