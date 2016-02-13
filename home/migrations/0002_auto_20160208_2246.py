# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='ImagePath',
            field=models.ImageField(verbose_name='Путь до изображения', upload_to='static/main_image/slider'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
