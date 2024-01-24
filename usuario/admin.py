from django.contrib import admin
from .models import usuario
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(usuario)
class userAdmin(ImportExportModelAdmin):
    list_display = ('nombre','apellidos','area','telefono')