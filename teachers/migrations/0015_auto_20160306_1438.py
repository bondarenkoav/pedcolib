# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0014_auto_20160306_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='alias',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='fullname'),
        ),
    ]
