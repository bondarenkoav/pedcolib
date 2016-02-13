# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20160208_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='link',
            field=models.CharField(max_length=100, default='', verbose_name='Ссылка на страницу'),
            preserve_default=False,
        ),
    ]
