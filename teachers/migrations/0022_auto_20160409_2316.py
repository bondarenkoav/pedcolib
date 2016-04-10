# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0021_teacher_photo_album'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher_photo_album',
            old_name='teacher',
            new_name='teacher_id',
        ),
    ]
