edad = int(input("Ingrese la edad: ")) 

if edad > 0:
    print("Edad no es un numero positivo")
elif edad < 18:
    print("No puedes ingresar")
elif edad <=30:
    print("Tienes que pagar USD 10")
elif edad <=60:
    print("Tienes un descuento del 20%")
else:
    print("Puedes entrar GRATIS!")

