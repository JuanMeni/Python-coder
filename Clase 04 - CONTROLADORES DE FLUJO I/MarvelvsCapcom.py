nombre = input("Ingrese su nombre: ")
fan = input ("Cual es tu preferencia...(M o C)?: ")

if(nombre[0]<"M" and fan == "M") or (nombre[0]>="N" and fan == "C"):
    print("Sos del grupo A")

else:
    print("Sos del grupo B")