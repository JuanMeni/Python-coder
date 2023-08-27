#1  Crear una función que reciba un número y una lista, e imprima {"Todos los valores son divisibles por {numero}"} si son todos divisibles, y {"Hay valores que no se pueden dividir por {numero}"} en caso contrario

def todos_divisibles(lista,num):
    for i in lista:
        if i % num != 0:
            return f"Hay valores que no se pueden dividir por {num}"
    return f"Todos los valores son divisibles por {num}"

print(todos_divisibles([4,8,10,20,30],2))