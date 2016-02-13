# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0011_auto_20160209_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='ImagePath',
            field=models.ImageField(upload_to='static/main_image/teachers', verbose_name='Путь до главного фото'),
        ),
    ]
