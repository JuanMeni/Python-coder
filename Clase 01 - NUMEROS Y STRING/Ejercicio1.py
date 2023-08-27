"""
Mi primer programa en Python

Consigna

Trabajas en Coderhouse y te piden crear un programa que calcule la nota final de estudiantes del curso de Python. La nota final se calcula basándonos en tres notas previas de las cuales, cada una corresponde un porcentaje distinto de la nota final. Los porcentajes se detallan a continuación: 

Los porcentajes asociados que debemos considerar de cada nota se detallan a continuación: 
- nota_1  cuenta como el 20% de la nota final
- nota_2 cuenta como el 30% de la nota final
- nota_3 cuenta como el 50% de la nota final

"""
print("Iniciando el programa")

nota_1=float(input("ingrese Nota 1 del alumno : "))
nota_2=float(input("ingrese Nota 2 del alumno : "))
nota_3=float(input("ingrese Nota 3 del alumno : "))


nota_final=(nota_1*0.2)+(nota_2*0.3)+(nota_3*0.5)

print(nota_final)
print("Su nota final es",nota_final)