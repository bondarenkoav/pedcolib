# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0010_auto_20160202_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='ImagePath',
            field=models.ImageField(height_field=300, width_field=200, blank=True, verbose_name='Путь до главного фото', upload_to='static/main_image/teachers'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='alias',
            field=models.CharField(blank=True, max_length=20, verbose_name='Алиас'),
        ),
    ]
