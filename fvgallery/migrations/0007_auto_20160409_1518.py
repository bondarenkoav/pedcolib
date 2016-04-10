# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fvgallery', '0006_auto_20160306_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='image',
        ),
        migrations.AddField(
            model_name='album',
            name='ImagePath',
            field=imagekit.models.fields.ProcessedImageField(verbose_name='Путь до изображения', upload_to='static/main_image/teachers', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='photo_thumb',
            field=imagekit.models.fields.ProcessedImageField(verbose_name='Путь до изображения', upload_to='static/main_image/teachers', default=''),
            preserve_default=False,
        ),
    ]
