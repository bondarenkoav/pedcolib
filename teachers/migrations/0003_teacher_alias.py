# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20151003_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='alias',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
