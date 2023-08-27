nacimiento = int(input("Ingrese su año de nacimiento: "))

if nacimiento >=1920 and nacimiento <=1940:
    print("Usted pertenece a la Generación Silenciosa")

elif nacimiento >=1946 and nacimiento <=1964:
    print("Usted pertenece a la Generación Baby Boomer")
elif nacimiento >=1965 and nacimiento <=1979:
    print("Usted pertenece a la Generación Baby Boomer")
elif nacimiento >=1980 and nacimiento <=2000:
    print("Usted pertenece a la Generación X")
elif nacimiento >=2001 and nacimiento <=2010:
    print("Usted pertenece a la Generación Z")

else:
    print("No existe generación asociada")