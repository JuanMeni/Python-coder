def calcula(op, a,b):
    if op == "sum":
        print(f"La suma de {a} + {b} es {a+b}")
    elif op == "res":
        print(f"La suma de {a} - {b} es {a-b}")
    elif op == "div":
        print(f"La suma de {a} / {b} es {a/b}")  
    elif op == "mul":
        print(f"La suma de {a} * {b} es {a*b}")
    else:
        print("Operación inválida")

print("Haciendo algunas cositas en la app..")

# calcula("sum",10,5)
# calcula("res",12,8)
# calcula("div",10,5)
# calcula("pot",3,-4)

op=input("Ingrese la operación a realizar: ")
op1=int(input("Ingrese el operador 1: "))
op2=int(input("Ingrese el operador 2: "))

calcula(op,op1,op2)

print("Haciendo cosas más importantes en la app..")

