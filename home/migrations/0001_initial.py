# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('ImagePath', models.ImageField(upload_to='', verbose_name='Путь до изображения')),
                ('title', models.CharField(max_length=100, verbose_name='Имя изображения')),
                ('description', models.TextField(verbose_name='Ссылка на страницу')),
            ],
            options={
                'db_table': 'Slider',
            },
        ),
    ]
