# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-23 18:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0007_auto_20180423_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='data_nascimento',
            field=models.DateField(default=datetime.datetime.now, null=True, verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='email',
            field=models.EmailField(default=None, max_length=255, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='nome',
            field=models.CharField(max_length=255, null=True, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='telefone',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Telefone'),
        ),
    ]
