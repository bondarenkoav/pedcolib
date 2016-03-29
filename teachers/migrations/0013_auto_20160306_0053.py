# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0012_auto_20160209_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='subject',
        ),
        migrations.AlterField(
            model_name='categoryqval',
            name='Name',
            field=models.CharField(max_length=100, verbose_name='Категория квалификации'),
        ),
        migrations.AlterField(
            model_name='degreys',
            name='Name',
            field=models.CharField(max_length=100, verbose_name='Степень'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='Name',
            field=models.CharField(max_length=100, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='ranks',
            name='Name',
            field=models.CharField(max_length=100, verbose_name='Звание'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='fullname',
            field=models.CharField(max_length=100, verbose_name='Фамилия Имя Отчество'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='teachers.Subject'),
        ),
    ]
