"""
URL configuration for AlmuerzoCLL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from usuario.views import loginUsuario, logoutUsuario, registrarUsuario
from django.contrib.auth.decorators import login_required
from lista.views import Home,regDiario,delRegAdmin,delRegDiario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/',include(('usuario.urls','usuario'))),
    path('lista/',include(('lista.urls','lista'))),
    path('', login_required(Home), name = 'index'),
    path('lista/reg/<int:id>',regDiario,name='regDiario'),
    path('lista/delreg/<int:id>',delRegDiario,name='delDiario'),
    path('lista/delAll/',delRegAdmin,name='delAll'),
    path('accounts/login/',loginUsuario.as_view(),name = "login"),
    path('usuario/regUser/',registrarUsuario.as_view(), name = 'regUser'),
    path('logout/',login_required(logoutUsuario), name= 'logout')
]
