from django.contrib import admin
from .models import Registro

class RegistroAdmin(admin.ModelAdmin):
    pass

admin.site.register(Registro, RegistroAdmin)
