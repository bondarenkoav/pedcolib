# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0023_auto_20160409_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_photo_album',
            name='descript',
            field=models.CharField(max_length=300, verbose_name='Описание фотографии', blank=True),
        ),
    ]
