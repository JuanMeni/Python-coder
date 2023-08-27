nombre = input("Ingrese su nombre: ")

if len(nombre) > 5:
    print("Se cumplio la condición")
    print("1. Su nombre es largo..")

    if nombre[0] == "V":
        print ("2. Su nombre empieza con V")
        
if nombre == nombre.capitalize():
    print ("3. Tu nombre está bien escrito")

print("Continua ejecutandose el resto del programa...")