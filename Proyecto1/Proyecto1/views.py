# hola mundo en django
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hello word")
