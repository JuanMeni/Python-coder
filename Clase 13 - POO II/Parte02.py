class Perro():

    num_patas = 4

    def __init__(self,nombre,raza,edad):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
    
    def __str__(self):
        return f'{self.raza} de {self.edad} años'
    
    def ladrar(self,cant):
        return 'guau'*cant
    
perro1 = Perro("Almita","Caniche",5)
 
# print(perro1.ladrar(8))

print(Perro.num_patas)
print(perro1.num_patas)
