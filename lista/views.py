from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import menu
from usuario.models import usuario
from django.template import RequestContext
from django.contrib import messages

# Create your views here.
@login_required
def Home(request):
    users = usuario.objects.filter(diario = True)

    return render(request, 'lista/index.html', {'users': users})
    
def regDiario(request, id):
    try:
        user = usuario.objects.get(pk = id)
    except user.DoesNotExist:
        return redirect(to='index')
    
    user.diario = True
    user.save()
    messages.add_message(request=request,level=messages.SUCCESS, message='Ya te registraste para el almuerzo de hoy!')
    return redirect(to='index')

def delRegDiario(request, id):
    try:
        user = usuario.objects.get(pk = id)
    except user.DoesNotExist:
        return redirect(to='index')
    
    user.diario = False
    user.save()
    messages.add_message(request=request,level=messages.SUCCESS, message='Fuiste eliminado de la lista de hoy satisfactoriamente.')
    return redirect(to='index')

def delRegAdmin(request):
    diarios = usuario.objects.filter(diario = True)

    for user in diarios:
        user.diario = False
        user.save()

    return redirect(to='index')

def verMenu(request):
    menus = menu.objects.all()

    return render(request, 'lista/index.html', {'menus': menus})

def cambiarMenu(request):
    entrada = request.GET.get('entrada')
    fondo = request.GET.get('fondo')
    postre = request.GET.get('postre')
    hipocal = request.GET.get('hipo')

    menus = menu.objects.get(pk = 1)
    menus.entrada = entrada
    menus.fondo = fondo
    menus.postre = postre
    menus.hipocal = hipocal
    menus.save()
    

    return redirect(to='index')