personas=[("Mauricio","Cuello",30),("Lionel","Messi",34),("Cristiano","Ronaldo",34),("Pepe","Mujica",40)]

for nombre, apellido, edad in personas:
    print(nombre)

paises=["Canada","USA","Mexico","Australia","Argentina","China","India","Singapur","Croacia","Corea del Sur"]

for pos,pais in enumerate(paises):
    print(pos)
    print(pais)

print(list(enumerate(paises)))

