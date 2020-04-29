from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request): # Primera vista
    doc_externo = open("C:/Users/danie/OneDrive/Escritorio/Proyecto COVID-19/HolaMundo/HolaMundo/templates/saludo.html") # Carga documento externo
    plt = Template(doc_externo.read()) # Crear plantilla a partir de documento externo
    doc_externo.close() # Cierra documento externo
    ctx = Context() # Creación del contexto (Datos adicionales que puede usar el template)
    documento = plt.render(ctx) # Renderizar el objeto Template pasandole el contexto

    return HttpResponse(documento)



def despedida(request):
    return HttpResponse("Chao mundo")

def dame_Fecha(request):
    fecha_actual = datetime.datetime.now()

    documento = """<html>
    <body>
    <h1>
    Fecha y hora actuales: %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return  HttpResponse(documento)

def calcula_Edad(request, edad, anio):
    periodo = anio - 2020
    edadFutura = edad + periodo
    documento = """<html>
    <body>
    <h2>
    En el año %s tendrás %s años
    </h2>
    </body>
    </html>""" %(anio, edadFutura)

    return HttpResponse(documento)