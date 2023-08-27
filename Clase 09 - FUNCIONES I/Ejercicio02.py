#2  Crear una función que reciba una lista y un número y retorne una lista con todos los números aumentados en el valor del número pasado como parametro

def suma_valor(lista,num):
    valores_aumentados=[]
    for i in lista:
        valores_aumentados.append(i+num)
    return valores_aumentados

print(suma_valor([10,20,30,40],5))