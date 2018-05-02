from django.db import models
from django.utils import timezone
from datetime import date
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Registro(models.Model):
    nome = models.CharField(('nome'), max_length=255, blank=True)
    data_nascimento = models.DateField(('Data de Nascimento'), default=date.today, blank=True)
    telefone = models.CharField(('Telefone'), max_length=255, default=None, blank=True)
    email = models.EmailField(('E-mail'), max_length=255, default=None, null=True)
    data_conversao = models.DateField(('Data de Conversão'), default=date.today, null=True)
    data_batismo = models.DateField(('Data de Batismo'), default=date.today, null=True)
    cep = models.CharField(('Cep'), max_length=8, default=None, null=True, blank=True)
    cidade = models.CharField(('Cidade'), max_length=255, default=None, blank=True)
    endereco = models.CharField(('Endereço'), max_length=255, default=None, blank=True)
    bairro = models.CharField(('Bairro'), max_length=255, default=None, blank=True )
    foto = models.FileField(upload_to='imagens/foto', default=None, null=True, blank=True)
    

# ESTADO CIVIL
    SOLTEIRO = 'Solteiro'
    CASADO = 'Casado'
    DIVORCIADO = 'Divorciado'
    SEPARADO = 'Separado'
    Estado_Civil = (
        (SOLTEIRO, 'Solteiro'),
        (CASADO, 'Casado'),
        (DIVORCIADO, 'Divorciado'),
        (SEPARADO, 'Separado'),
    )
    estado_civil = models.CharField(('Estado Civil'),
        max_length=100,
        choices=Estado_Civil,
        default='',
        blank=True
    )

    def __str__(self):
        return u"%s" % self.nome