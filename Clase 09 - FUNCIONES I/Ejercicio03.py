#3  Crear una función que reciba una tupla de palabras y retorne una frase uniendo esas palabras separadas por un espacio



def crea_frase(palabras):
    resultado= ""
    for palabra in palabras:
        resultado += " " + palabra
    return resultado
    
print(crea_frase(("Hola","alumnos!","paguen","el","asado")))