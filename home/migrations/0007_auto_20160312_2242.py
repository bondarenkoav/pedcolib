# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20160227_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='image',
        ),
        migrations.AddField(
            model_name='slider',
            name='ImagePath_resize',
            field=imagekit.models.fields.ProcessedImageField(verbose_name='Путь до изображения', default='', upload_to='static/main_image/slider'),
            preserve_default=False,
        ),
    ]
