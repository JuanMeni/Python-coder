def calcula(op, a,b):
    if op == "sum":
        # print(f"La suma de {a} + {b} es {a+b}")
        return a+b
    elif op == "res":
        # print(f"La suma de {a} - {b} es {a-b}")
        return a-b
    elif op == "div":
        print(f"La suma de {a} / {b} es {a/b}")  
    elif op == "mul":
        print(f"La suma de {a} * {b} es {a*b}")
    else:
        print("Operación inválida")

res1=calcula("sum",10,5)
res2=calcula("res",8,5)

print(res1+res2)