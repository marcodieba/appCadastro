# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-23 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0008_auto_20180423_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='bairro',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='endereco',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Endereço'),
        ),
    ]
