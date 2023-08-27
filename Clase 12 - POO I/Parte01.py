class Persona():
    
    def __init__(self,nom,ape,ed):
        self.nombre=nom
        self.apellido=ape
        self.edad=ed
        
    def saluda(self):
        return f'Hola, mi nombre es {self.nombre} {self.apellido}'
    
persona1=Persona("Mauricio","Cuello",32)
persona2=Persona("Leonel","Messi",36)

print(persona1.saluda())
print(persona2.saluda())
    