# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0003_auto_20150927_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduate',
            name='postandarea',
            field=models.TextField(blank=True),
        ),
    ]
