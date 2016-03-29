# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0013_auto_20160306_0053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Предмет ', 'verbose_name_plural': 'Список предметов '},
        ),
        migrations.AlterModelTable(
            name='subject',
            table='subject',
        ),
    ]
