# hola mundo en django
from datetime import date
from django.http import HttpResponse
import datetime

def saludo(request):
    
    documento="""
    <html>
    <body>
    <h1>
    Hello world, welcome to the project. 
    </h1>
    <body>
    <html>"""
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("goodbye word")

def fecha(request,):
    
    fecha=datetime.datetime.now()
    