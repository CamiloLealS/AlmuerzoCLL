from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class usuarioManager(BaseUserManager):
    def create_user(self,email, username, nombre, apellidos, password = None):
        if not email:
            raise ValueError('Debe poseer un Correo Electrónico')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            nombre = nombre,
            apellidos = apellidos
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, nombre, apellidos, password):
        user = self.create_user(
            email,
            username=username,
            nombre = nombre,
            apellidos=apellidos
        )
        user.usuario_admin = True
        user.set_password(password)
        user.save()
        return user
        


class usuario(AbstractBaseUser):
    username = models.CharField('Nombre de Usuario',unique=True, max_length=50)
    email = models.EmailField('Correo Electrónico',unique=True, max_length=254)
    nombre = models.CharField('Nombre', max_length=50,blank=True, null=True)
    apellidos = models.CharField('Apellidos',max_length=200, blank=True, null=True)
    areas = (('Área','Área'),
            ('CALIDAD','CALIDAD'),
            ('CENTROS MÉDICOS','CENTROS MÉDICOS'),
            ('DOCTORES CENTROS MÉDICOS','DOCTORES CENTROS MÉDICOS'),
            ('ESTERILIZACIÓN','ESTERILIZACIÓN'),
            ('GERENCIA ADMINISTRACIÓN','GERENCIA ADMINISTRACIÓN'),
            ('GERENCIA GENERAL','GERENCIA GENERAL'),
            ('GERENCIA FINANZAS','GERENCIA FINANZAS'),
            ('GERENCIA AMBULATORIA','GERENCIA AMBULATORIA'),
            ('GERENCIA DE SALUD','GERENCIA DE SALUD'),
            ('GERENCIA COMERCIAL','GERENCIA COMERCIAL'),
            ('LABORATORIO','LABORATORIO'),
            ('MATERNIDAD/NEO','MATERNIDAD/NEO'),
            ('PABELLÓN','PABELLÓN'),
            ('UNIDAD DE EXAMENES','UNIDAD DE EXAMENES'),
            ('UNIDAD HOSPITALIZACIÓN','UNIDAD HOSPITALIZACIÓN'),
            ('UTI','UTI'),
            ('URGENCIA/RECEPCIÓN DE URGENCIAS','URGENCIA/RECEPCIÓN DE URGENCIAS'),
            ('OTRAS UNIDADES','OTRAS UNIDADES'))
    area = models.CharField('Área',max_length = 100, choices = areas, default = 'Área', null = True)
    telefono = models.CharField('Teléfono', max_length =13 , blank = True, null = True)
    hipo = models.BooleanField(default = False)
    diario = models.BooleanField(default = False)
    usuario_activo = models.BooleanField(default= True)
    usuario_admin = models.BooleanField(default=False)
    objects = usuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombre','apellidos']

    def __str__(self) -> str:
        return self.nombre + ' ' + self.apellidos
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_admin
    