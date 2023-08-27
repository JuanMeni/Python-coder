# ELD - Escribir un programa que pregunte al usuario numeros hasta que ingrese el 0, en ese momento devolver la suma de todos los numeros ingresados

numero = int(input("Ingrese un numero: "))
acumulador = 0

while numero!=0:
    acumulador += numero
    numero=int(input("Ingrese un numero: "))

print(acumulador)