# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_teacher_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='ImagePath',
            field=models.ImageField(upload_to='', height_field=300, blank=True, width_field=200),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='article',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
