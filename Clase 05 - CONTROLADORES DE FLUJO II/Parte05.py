# ELD - Escribir un programa que pregunte al usuario valores hasta que ingrese el 0, devolver la suma de los numeros ingresados pero sin tener en cuenta los numeros que sean divisibles por 3 - usar continue

numero = int(input("Ingrese un numero: "))
acumulador = 0

while numero!=0:
    if numero %3 == 0:
        numero=int(input("Ingrese un numero: "))
        continue
    acumulador += numero
    numero=int(input("Ingrese un numero: "))

print(acumulador)