# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publics',
            name='link',
            field=models.CharField(max_length=30, blank=True, verbose_name='Ссылка на источник'),
        ),
    ]
