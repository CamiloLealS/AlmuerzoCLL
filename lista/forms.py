from django import forms
from .models import menu


class menuForm(forms.ModelForm):
    class Meta:
        model = menu
        fields = ['entrada','fondo','postre','hipocal']