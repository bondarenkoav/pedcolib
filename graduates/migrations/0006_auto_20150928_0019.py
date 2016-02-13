# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0005_graduate_imagepath'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graduate',
            name='middlename',
        ),
        migrations.RemoveField(
            model_name='graduate',
            name='name',
        ),
        migrations.RemoveField(
            model_name='graduate',
            name='surname',
        ),
        migrations.AddField(
            model_name='graduate',
            name='fullname',
            field=models.CharField(max_length=80, blank=True, verbose_name='Ваше ФИО'),
        ),
        migrations.AddField(
            model_name='graduate',
            name='veryfid_data',
            field=models.BooleanField(default=False, verbose_name='Данные верны'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='ImagePath',
            field=models.ImageField(height_field=300, upload_to='', blank=True, width_field=200, verbose_name='Ваше фото'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='article',
            field=models.TextField(verbose_name='Несколько слов о себе'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='postandarea',
            field=models.TextField(blank=True, verbose_name='Где и кем работаете'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='soglasie',
            field=models.BooleanField(verbose_name='Даю согласие на обработку личных данных'),
        ),
    ]
