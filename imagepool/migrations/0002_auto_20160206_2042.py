# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagepool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepool',
            name='image',
            field=models.ImageField(upload_to='static/img/imagepool/%Y/%m', verbose_name='Изображение'),
        ),
    ]
