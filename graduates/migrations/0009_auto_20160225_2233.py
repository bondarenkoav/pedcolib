# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0008_auto_20160210_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='graduate',
            options={'verbose_name_plural': 'Выпускники', 'ordering': ['fullname'], 'verbose_name': 'Выпускник'},
        ),
    ]
