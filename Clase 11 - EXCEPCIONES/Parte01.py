print("Iniciando mi aplicación..")

print("Hola mundo!")

a=int(input("Ingrese el numerador: "))
b=int(input("Ingrese el denominador: "))

def divide(op1,op2):
    if op2!=0:
        return op1/op2
    else:
        return None

print(divide(a,b))

print("Continuando mi aplización..")