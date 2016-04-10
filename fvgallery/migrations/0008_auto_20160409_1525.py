# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fvgallery', '0007_auto_20160409_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='photo_thumb',
        ),
        migrations.AlterField(
            model_name='album',
            name='ImagePath',
            field=imagekit.models.fields.ProcessedImageField(verbose_name='Путь до изображения', upload_to='static/main_image/photo/album_image'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(verbose_name='Путь до изображения', upload_to='static/main_image/photo/images/'),
        ),
    ]
