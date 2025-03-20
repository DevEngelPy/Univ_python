class RegEmp:
    def __init__(self):
        pass
    
    def gen_reg(self) -> dict:
        __nombre:str = input('nombre: ')   
        __edad:int = int(input('edad: '))
        __saliario:float = float(input('salario: '))
        __es_jefe:str = input('es jefe? (si/no): ')
        __es_jefe = __es_jefe.lower() == 'si'
        
        datos:dict = {
            'nombre:':__nombre,
            'edad':__edad,
            'salario':__saliario,
            'es_jefe':__es_jefe
        }
        return datos
    
    def __str__(self):
        return f'Datos: {self.gen_reg()}'

from random import randint
class GenId:
    def __init__(self):
        pass
    
    def gen(self) -> str:
        __nombre:str = input('nombre:')
        __apellido:str = input('apellido: ')
        __ani_nacimiento:str = input('año de nacimiento: ')
        normalisacion:dict = self.__normalizacion(nombre=__nombre, apellido=__apellido, anio=__ani_nacimiento)
        
        return f'{normalisacion['nombre']}{normalisacion['apellido']}{normalisacion['año']}{normalisacion['id']}'
        
    def __normalizacion(self,nombre:str, apellido:str,anio:str) -> dict:
        id_unico:int = randint(1000,9999)
        dato:dict = {
            'nombre':nombre.strip().upper()[0:2],
            'apellido':apellido.strip().upper()[0:2],
            'año':anio.strip()[2:4],
            'id':id_unico
        }
        return dato
        
    def __str__(self) -> str:
        return f'data: {self.gen()}'   
    
    
if __name__ == '__main__':
   nuevo_id:object = GenId()
   print(nuevo_id)