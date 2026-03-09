from django.shortcuts import render, HttpResponse


# Create your views here.
def servicioPrincipal(request):
    return HttpResponse("Hola")