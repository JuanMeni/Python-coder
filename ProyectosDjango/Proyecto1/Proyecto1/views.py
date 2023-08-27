from django.http import HttpResponse 
from datetime import datetime
from django.template import Template, Context


# Una funcion para mostrar un msj en mi pagina
def saludo(req):
    return HttpResponse("Hola a todos desde mi primer aplicaion de Django!")

# Ejemplo de otra url
def segundaVista(req):
    return HttpResponse("""
        <h1>Bienvenida a mi primer web</h1>
        <br>
        <br>
        <p>Esto esta muy bueno!</p>
        """
    )

def diaDeHoy(req):
    dia = datetime.now()
    documentoDeTexto = f'Hoy es: {dia}'
    return HttpResponse(documentoDeTexto)

def saluda_con_nombre(req, nombre):
    documentoDeTexto = f'Mi nombre es: {nombre}'
    return HttpResponse(documentoDeTexto)

def probando_template(req):
    # Verificar que a la hora de copiar la direccion del template use "/" en vez de "\"
    miHtml = open("C:/Users/Juan/Desktop/Python-CODER/ProyectosDjango/Proyecto1/Proyecto1/templates/templates1.html") #Sale SyntaxError si lleva el "\" en vez de "/"
    plantilla = Template(miHtml.read())
    miHtml.close()
    
    miContexto = Context()
    
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)