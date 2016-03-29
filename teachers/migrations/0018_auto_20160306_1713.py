# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0017_auto_20160306_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryqval',
            name='visible',
        ),
        migrations.RemoveField(
            model_name='degreys',
            name='visible',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='visible',
        ),
        migrations.RemoveField(
            model_name='ranks',
            name='visible',
        ),
    ]
