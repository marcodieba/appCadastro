from django.forms import ModelForm
from .models import Registro

class RegistroForm(ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'