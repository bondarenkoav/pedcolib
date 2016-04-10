# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0019_auto_20160403_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='ImagePath',
            field=imagekit.models.fields.ProcessedImageField(verbose_name='Путь до изображения', upload_to='static/main_image/teachers'),
        ),
    ]
