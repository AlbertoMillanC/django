# hola mundo en django
from datetime import date
from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    
    def __init__(self, nombre, apellido,):
        
        self.nombre = nombre
        
        self.apellido = apellido
        
       

def saludo(request):
    
    p1=Persona("Profesor Juan","Perez")
    
    #nombre = "Juan"
    #apellido = "Perez"
    lenguajes_programcion = ["HTML","CSS","JavaScript","Python","PHP"]
    ahora=datetime.datetime.now()

    
    doc_externo=open("Proyecto1/templates/saludo.html")
    
    plt=Template(doc_externo.read())
    
    doc_externo.close()
   
    ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"tiempo":ahora,"temas":lenguajes_programcion })      
    
    documento=plt.render(ctx)
   
    return HttpResponse(documento)


def despedida(request):
    return HttpResponse("goodbye word")

def dameFecha(request):
    
    fecha_actual=datetime.datetime.now()
    
    documento="""
    <html>
    <body>
    <h2>
    Date and time: %s
    </h2>
    <body>
    <html>""" %fecha_actual 
    
    return HttpResponse(documento)

def calculaEdad(request,edad,agno):
    
    periodo=agno-2022
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendras %s años" %(agno, edadFutura)
    
    return HttpResponse(documento)