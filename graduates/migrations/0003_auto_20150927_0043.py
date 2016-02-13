# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0002_auto_20150925_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graduate',
            name='author',
        ),
        migrations.RemoveField(
            model_name='graduate',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='graduate',
            name='tags',
        ),
        migrations.AddField(
            model_name='graduate',
            name='postandarea',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='graduate',
            name='soglasie',
            field=models.BooleanField(default=''),
            preserve_default=False,
        ),
    ]
