#Crear un programa que pida números al usuario hasta que ingrese el "0"
#   Imprimir por pantalla la lista de valores ingresados
#   Recorrer la lista de valores ingresados y crear una nueva lista teniendo en cuenta los siguientes casos
#   Si el valor leido es positivo impar agregar su doble, es decir, multiplicarlo por dos y agregarlo a la nueva lista
#   Si el valor leido es positivo par no tenerlo en cuenta
#   Si el valor leido es negativo finalizar el programa y devolver los elementos que tiene la nueva lista hasta ese momento

numero=int(input("Ingrese un numero: "))
lista_numeros=[]
lista_nueva=[]

while numero != 0:
    lista_numeros.append(numero)
    numero=int(input("Ingrese un numero: "))

print(lista_numeros)

for numero in lista_numeros:
    if numero>0 and numero%2 !=0:
        lista_nueva.append(numero*2)
    if numero<0:
        break

print(lista_nueva)



    


    
