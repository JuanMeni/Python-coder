texto = input ("Ingrese lo que quiere escribir: ")
f = open('Clase 08 - MANEJO DE ARCHIVOS Y DATOS/texto.txt', 'a')
f.write(texto)
f.close()  

