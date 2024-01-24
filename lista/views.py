from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from .models import menu
from .forms import menuForm
from usuario.models import usuario
from django.template import RequestContext
from django.contrib import messages

# Create your views here.
@login_required
def Home(request):
    users = usuario.objects.filter(diario = True)
    menu_dia = menu.objects.first()

    return render(request, 'lista/index.html', {'users': users, 'menu_dia' : menu_dia})
    
def regDiario(request, id):
    try:
        user = usuario.objects.get(pk = id)
    except user.DoesNotExist:
        return redirect(to='index')
    
    user.diario = True
    user.save()
    messages.add_message(request=request,level=messages.SUCCESS, message='Estás registrad@ para el almuerzo de hoy!')
    return redirect(to='index')

def delRegDiario(request, id):
    try:
        user = usuario.objects.get(pk = id)
    except user.DoesNotExist:
        return redirect(to='index')
    
    user.diario = False
    user.save()
    messages.add_message(request=request,level=messages.SUCCESS, message='Fuiste eliminad@ de la lista de hoy satisfactoriamente.')
    return redirect(to='index')

def delRegAdmin(request):
    diarios = usuario.objects.filter(diario = True)

    for user in diarios:
        user.diario = False
        user.save()

    return redirect(to='index')

def cambiarMenu(request):
    if request.method == 'POST':
        form = menuForm(request.POST)
        if form.is_valid():
            menu.objects.all().delete()
            form.save()
            print(menu.objects.first())

            return redirect(to='index')
    else:
        form = menuForm()
    
    return render(request, 'lista/index.html',{'form':form})

