from django.forms import ModelForm
from .models import Registro
from django import forms


class RegistroForm(ModelForm):
    class Meta:
        model = Registro
        # data_nascimento = forms.DateField(input_formats=['%m/%d/%Y'])
        fields = '__all__'
        