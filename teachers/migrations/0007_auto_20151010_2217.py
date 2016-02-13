# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0006_auto_20151010_2158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryqval',
            options={'verbose_name': 'Категория квалификации', 'verbose_name_plural': 'Виды категорий квалификации'},
        ),
        migrations.AlterModelOptions(
            name='degreys',
            options={'verbose_name': 'Степень', 'verbose_name_plural': 'Виды степеней'},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name': 'Должность', 'verbose_name_plural': 'Виды должностей'},
        ),
        migrations.AlterModelOptions(
            name='ranks',
            options={'verbose_name': 'Звание', 'verbose_name_plural': 'Виды званий'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Персоналий', 'verbose_name_plural': 'Персоналии'},
        ),
        migrations.AddField(
            model_name='categoryqval',
            name='visible',
            field=models.BooleanField(verbose_name='Отображение на сайте', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='degreys',
            name='visible',
            field=models.BooleanField(verbose_name='Отображение на сайте', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='visible',
            field=models.BooleanField(verbose_name='Отображение на сайте', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ranks',
            name='visible',
            field=models.BooleanField(verbose_name='Отображение на сайте', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoryqval',
            name='Description',
            field=models.TextField(verbose_name='Описание', blank=True),
        ),
        migrations.AlterField(
            model_name='categoryqval',
            name='Name',
            field=models.CharField(verbose_name='Категория квалификации', max_length=20),
        ),
        migrations.AlterField(
            model_name='degreys',
            name='Description',
            field=models.TextField(verbose_name='Описание', blank=True),
        ),
        migrations.AlterField(
            model_name='degreys',
            name='Name',
            field=models.CharField(verbose_name='Степень', max_length=20),
        ),
        migrations.AlterField(
            model_name='posts',
            name='Description',
            field=models.TextField(verbose_name='Описание', blank=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='Name',
            field=models.CharField(verbose_name='Должность', max_length=20),
        ),
        migrations.AlterField(
            model_name='ranks',
            name='Description',
            field=models.TextField(verbose_name='Описание', blank=True),
        ),
        migrations.AlterField(
            model_name='ranks',
            name='Name',
            field=models.CharField(verbose_name='Звание', max_length=20),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='ImagePath',
            field=models.ImageField(verbose_name='Путь до главного фото', width_field=200, upload_to='', blank=True, height_field=300),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='alias',
            field=models.CharField(verbose_name='Алиас', max_length=20),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='fullname',
            field=models.CharField(verbose_name='Фамилия Имя Отчество', max_length=80),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(blank=True, verbose_name='Предметы', max_length=30),
        ),
    ]
