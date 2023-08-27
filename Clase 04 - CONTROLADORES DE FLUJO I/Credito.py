edad = int(input("Ingrese la edad del cliente: "))
antiguedad = int(input("Ingrese la antiguedad del cliente: "))
salario = int(input("Ingrese el salario, en dolares, del cliente: "))

if edad >=18:
    if antiguedad <= 3:
        if salario >= 2500:
            print("Credito APROBADO")
    elif salario >= 4000:
        print("Crédito APROBADO")
    else:
        print("Credito RECHAZADO")
else:
    print("Crédito RECHAZADO por ser menor de edad")


