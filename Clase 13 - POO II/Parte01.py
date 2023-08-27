"""
1. Definir la clase
2. Definir el metodo constructor (Atributos)
3. Dar un comportamiento a la clase (Funcion). Todos los metodos de cualquier clase reciben de manera obligatoria el "self"
4. Definir el objeto o tipo de dato (Propio de la clase)
"""

class Persona():

    def __init__(self,nom,ape,ed,ami):
        self.nombre=nom
        self.apellido=ape
        self.edad=ed
        self.amigos=ami

    def saluda(self):
        return f'Hola soy {self.nombre} {self.apellido} y tengo {self.edad} años'
    
    def lista_amigos(self):
        mis_amigos=[]
        for persona in self.amigos:
            mis_amigos.append(persona.nombre)
        lista_nombres=' '.join(mis_amigos)
        return f'Soy amigo de {lista_nombres}'

persona1=Persona("Roman","Riquelme",42, None)
persona2=Persona("Lionel","Messi",36,None)
persona3=Persona("Cristiano","Ronaldo",39,None)
persona4=Persona("Mauricio","Cuello",32,[persona1,persona2,persona3])

# print(persona1.nombre)
# print(persona1.nombre,persona1.edad)     
# print(persona2.apellido)

# print(persona1.saluda("Veronica","Menichetti",37))

print(persona1.saluda())
print(persona2.saluda())
print(persona3.saluda())

print(persona4.lista_amigos())