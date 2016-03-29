# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20160225_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='ImagePath',
            new_name='image',
        ),
    ]
