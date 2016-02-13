# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0007_auto_20151004_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduate',
            name='ImagePath',
            field=models.ImageField(blank=True, verbose_name='Ваше фото', upload_to='static/main_image/graduates'),
        ),
    ]
