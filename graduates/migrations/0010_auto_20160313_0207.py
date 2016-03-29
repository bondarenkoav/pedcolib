# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0009_auto_20160225_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graduate',
            name='ImagePath',
        ),
        migrations.AlterField(
            model_name='graduate',
            name='postandarea',
            field=imagekit.models.fields.ProcessedImageField(upload_to='static/main_image/graduates', verbose_name='Ваше фото'),
        ),
    ]
