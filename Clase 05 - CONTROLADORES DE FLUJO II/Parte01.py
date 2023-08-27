"""WHILE y BREAK"""

n=int(input("Ingresa un limite: "))
i = 1


while i < n:
    if i > 10:
        break
    print(i)
    i = i + 1
else:
    print("Se imprimieron todos los números")

print("Continuamos con nuestro programa...")

