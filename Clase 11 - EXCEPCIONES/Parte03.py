print("Iniciando mi aplicación..")

while True:
    try:
        peso=float(input("Ingrese su peso: ")) 
        altura=float(input("Ingrese su altura: "))
        imc=peso/altura**2
        print(imc)
        break
    except:
        print("Ingreso valores incorrectos, intentelo de nuevo..")

print("Continuando mi aplicación..")