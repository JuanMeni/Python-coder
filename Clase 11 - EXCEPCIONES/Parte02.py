print("Iniciando mi aplicación..")

try:
    nombre=input("Ingrese su nombre: ")
    edad=int(input("Ingrese su edad: "))
    print(f'Hola {nombre}, el año que viene tendrás {edad+1} años')
except:
    print("No ingresaste una edad correcta")

print("Continuando mi aplicación..")