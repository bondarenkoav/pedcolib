# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0009_auto_20160131_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='_article_rendered',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='article',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Текст статьи'),
        ),
    ]
