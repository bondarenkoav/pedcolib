# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fvgallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='img',
        ),
        migrations.AddField(
            model_name='photo',
            name='photo',
            field=models.ImageField(verbose_name='Фото', default='', upload_to='static/main_image/gallery'),
            preserve_default=False,
        ),
    ]
