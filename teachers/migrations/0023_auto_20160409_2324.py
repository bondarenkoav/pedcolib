# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0022_auto_20160409_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher_photo_album',
            old_name='teacher_id',
            new_name='teacher',
        ),
    ]
