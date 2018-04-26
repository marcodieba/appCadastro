# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-23 18:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0009_auto_20180423_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='bairro',
            field=models.CharField(blank=True, default=None, max_length=255, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='cep',
            field=models.CharField(blank=True, default=None, max_length=8, null=True, verbose_name='Cep'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='cidade',
            field=models.CharField(blank=True, default=None, max_length=255, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='data_nascimento',
            field=models.DateField(blank=True, default=datetime.datetime.now, verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='endereco',
            field=models.CharField(blank=True, default=None, max_length=255, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='foto',
            field=models.FileField(default=None, null=True, upload_to='imagens/foto'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='nome',
            field=models.CharField(blank=True, max_length=255, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='telefone',
            field=models.CharField(blank=True, default=None, max_length=255, verbose_name='Telefone'),
        ),
    ]