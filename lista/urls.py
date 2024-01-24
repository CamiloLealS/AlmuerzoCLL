from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import Home, regDiario, delRegAdmin, delRegDiario,cambiarMenu

urlpatterns = [
    path('', login_required(Home),name='index'),
    path('lista/reg/<int:id>',regDiario, name='regDiario'),
    path('lista/delreg/<int:id>',delRegDiario,name='delDiario'),
    path('lista/delAll/',delRegAdmin,name='delAll'),
    path('lista/edit/',cambiarMenu, name= 'editMenu')
]
