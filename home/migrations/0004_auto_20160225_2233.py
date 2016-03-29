# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_slider_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name_plural': 'Слайды', 'ordering': ['title'], 'verbose_name': 'Слайд'},
        ),
    ]
