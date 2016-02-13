# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0007_auto_20151010_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='article',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Текст статьи'),
        ),
    ]
