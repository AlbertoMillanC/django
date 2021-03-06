# hola mundo en django
from datetime import date
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
class Persona(object):
    
    def __init__(self, nombre, apellido,):
        
        self.nombre = nombre
        
        self.apellido = apellido
        
def pagina1(request):
    
    return render(request,"pagina1.html")

def pagina2(request):
    
    return render(request,"pagina2.html")
        

def saludo(request):
    
    p1=Persona("Profesor Alberto","Millán")
    
    #nombre = "Juan"
    #apellido = "Perez"
    lenguajes_programcion = ["HTML","CSS","JavaScript","Python","PHP"]
    ahora=datetime.datetime.now()

    
    #doc_externo=open("Proyecto1/templates/saludo.html")
    
    #plt=Template(doc_externo.read())
    
    #doc_externo.close()
    
    #doc_externo=get_template("saludo.html")
   
    #ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"tiempo":ahora,"temas":lenguajes_programcion })      
    
    #documento=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"tiempo":ahora,"temas":lenguajes_programcion })
   
    return render(request,"saludo.html",{"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"tiempo":ahora,"temas":lenguajes_programcion })


def despedida(request):
    return render("goodbye word")

def dameFecha(request):
    
    fecha_actual=datetime.datetime.now(+1)
    
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