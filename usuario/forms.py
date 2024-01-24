from typing import Any
from django import forms 
from django.contrib.auth.forms import AuthenticationForm
from .models import usuario
from django.contrib import messages


class FormLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class userForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Ingrese su contraseña...',
            'id' : 'password1',
            'required' : 'required',
        }
        
    ))
    password2 = forms.CharField(label='Confirmar Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Ingrese nuevamente su contraseña...',
            'id' : 'password2',
            'required' : 'required',
        }
        
    ))

    class Meta:
        model = usuario
        fields = ['nombre','apellidos','email','area','telefono','hipo']

        widgets = {
            'nombre' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Nombre',
                    'required' : 'required'
                }
            ),
            'apellidos' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Apellidos',
                    'required' : 'required'
                }
            ),
            'email' : forms.EmailInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Correo Electrónico',
                    'id' : 'email',
                    'required' : 'required'
                }
            ),
            'area' : forms.Select(
                attrs = {
                    'class' : 'form-select',
                    'style' : 'display:block; width:80%',
                    'placeholder' : 'Área',
                    'required' : 'required'
                }
            ),
            'telefono' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Teléfono',
                    'required' : 'required'
                }
            ),
            'hipo' : forms.CheckboxInput(
                attrs = {
                    'class' : 'form-check-input'
                }
            )
        }
        labels = {
            'siempre':'Solicitar a diario el almuerzo automáticamente',
            'hipo' :'Solicitar menú hipocalórico(Favor de marcar con antecedentes médicos ya presentados)'
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@clinicalosleones' not in email:
            raise forms.ValidationError('Correo electrónico no pertenece a Clínica Los Leones')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2
    
    def save(self, commit = True):
        user = super().save(commit=False)
        user.username = user.email.split('@')[0]
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user