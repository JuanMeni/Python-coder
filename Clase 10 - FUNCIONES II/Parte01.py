def saluda(nombre,apellido):
    return f"Hola, me llamo {nombre} {apellido}"

print(saluda("Mauricio","Cuello"))
print(saluda("Cuello","Mauricio"))
#la identificacion del parámetro no es posicional
print(saluda(apellido="Cuello", nombre="Mauricio"))
print(saluda(nombre="Mauricio",apellido="Cuello"))

