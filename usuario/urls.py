from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import registrarUsuario

urlpatterns = [
    path('user/register',registrarUsuario.as_view(), name='regUser')
]
