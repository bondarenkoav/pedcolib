# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_auto_20151010_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='tags',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
