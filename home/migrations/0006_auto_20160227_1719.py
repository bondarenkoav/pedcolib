# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20160225_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='description',
            field=models.TextField(verbose_name='Описание', blank=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='link',
            field=models.CharField(verbose_name='Ссылка на страницу', max_length=100, blank=True),
        ),
    ]
