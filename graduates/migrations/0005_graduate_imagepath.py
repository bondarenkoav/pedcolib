# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0004_auto_20150927_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='graduate',
            name='ImagePath',
            field=models.ImageField(height_field=300, default='', width_field=200, upload_to=''),
            preserve_default=False,
        ),
    ]
