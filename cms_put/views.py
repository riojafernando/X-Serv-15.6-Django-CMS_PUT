from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound
from models import Pages

# Create your views here.
@csrf_exempt
def mostrar(request, recurso):
    if request.method == "GET":
        try:
            fila = Pages.objects.get(name=recurso)
            return HttpResponse(request.method + " " + str(fila.id) +
                    "     "  + fila.name + fila.page)
        except Pages.DoesNotExist:
            return HttpResponseNotFound('Page not found' + recurso)

    elif request.method == "PUT":
        try:
            cuerpo = request.body
            fila = Pages.objects.create(name=recurso, page=cuerpo)
            fila.save()
            return HttpResponse("Nueva Fila")
        except:
            return HttpResponseNotFound("Error")
