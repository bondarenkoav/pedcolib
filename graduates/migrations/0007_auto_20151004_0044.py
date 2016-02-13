# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0006_auto_20150928_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduate',
            name='veryfid_data',
            field=models.BooleanField(default=False, verbose_name='Данные подтверждены администратором сайта'),
        ),
    ]
