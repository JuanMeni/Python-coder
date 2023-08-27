class Persona():

    def __init__(self,nombre,apellido,edad,dni):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.dni=dni

    def saluda(self):
        return f'Hola, me llamo {self.nombre} {self.apellido}'

class Empleado(Persona):

    def __init__(self,nombre,apellido,edad,dni,sueldo,horario):
        super().__init__(nombre,apellido,edad,dni)
        # self.nombre=nombre
        # self.apellido=apellido
        # self.edad=edad
        # self.dni=dni
        self.sueldo=sueldo
        self.horario=horario

    def fichar(self,ingreso):
        if ingreso < self.horario:
            return f'Llegue {self.horario - ingreso} minutos temprano'
        else:
            return f'Llegue {ingreso - self.horario} minutos tarde'

class Seguridad():

    def __init__(self,nombre,apellido,edad,dni,sueldo,horario,vehiculo, arma):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.dni=dni
        self.sueldo=sueldo
        self.horario=horario
        self.vehiculo=vehiculo
        self.arma=arma
    
    def saluda(self):
        return f'Hola, me llamo {self.nombre} {self.apellido}'
    
    def fichar(self,ingreso):
        if ingreso < self.horario:
            return f'Llegue {self.horario - ingreso} minutos temprano'
        else:
            return f'Llegue {ingreso - self.horario} minutos tarde'
    
    def llamar_policia(self,mensaje):
        return f'Llamo a la policia y les digo {mensaje}'
    
persona1=Persona('Mauricio','Cuello',32,123123)
Empleado1=Empleado('Cristiano','Ronaldo',39,121212,1700,480)
Seguridad1=Seguridad('Lionel','Messi',36,321321,1900,420, 'Fiat 600', 'AK-47')   

print(persona1.saluda())
print(Empleado1.saluda())
print(Seguridad1.saluda())