#Escribir un programa donde el usuario tiene que adivinar un numero, si adivina, imprimir el mensaje "Adivinaste", sino lo logra darle otra oportunidad hasta llegar a 3 oportunidades, en caso de que no adivine imprimir "Se te acabaron las oportunidades" - Usar while-else

numero_secreto = 5
intentos = 1
numero = int(input("Ingrese un numero: "))

while numero != numero_secreto:
    if intentos == 3: 
        print("Se te acabaron los intentos")
        break
    else:
        numero = int(input("Ingrese otro numero: "))
        intentos += 1
else:
    print("ADIVINASTE!!!") 