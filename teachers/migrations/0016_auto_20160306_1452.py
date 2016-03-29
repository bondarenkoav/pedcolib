# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0015_auto_20160306_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='post',
        ),
        migrations.AddField(
            model_name='teacher',
            name='post',
            field=models.ManyToManyField(blank=True, to='teachers.Posts'),
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='rank',
        ),
        migrations.AddField(
            model_name='teacher',
            name='rank',
            field=models.ManyToManyField(blank=True, to='teachers.Ranks'),
        ),
    ]
