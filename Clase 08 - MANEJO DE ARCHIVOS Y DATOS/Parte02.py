persona = {
    "nombre" : None,
    "apellido" : None,
    "edad" : None

}

for dato in persona.keys():
  persona [dato] = input (f"Ingrese su {dato}: ")

f = open('Clase 08 - MANEJO DE ARCHIVOS Y DATOS/texto2.txt', 'w')

for valor in persona.values():
  f.write(valor + "")
f.close