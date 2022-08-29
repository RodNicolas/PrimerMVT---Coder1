from contextvars import Context
from string import Template
from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import HttpResponse

def familia(request):
    return HttpResponse("¡Bienvenidos a la página de la familia Citrus!")

def miembrosFamilia(self):
    
    miHtml = open(r"C:\Users\Sonni\OneDrive\Escritorio\PrimerMVT\PrimerPagina\PrimerPagina\Plantillas\template.html")
    
    plantilla = Template(miHtml.read())
    
    miHtml.close()
    
    miContexto = Context()
    
    documento = plantilla.render(miContexto)
    
    return HttpResponse(documento)
    