# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0018_auto_20160306_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='ImagePath',
            field=imagekit.models.fields.ProcessedImageField(upload_to='static/main_image/slider', verbose_name='Путь до изображения'),
        ),
    ]
