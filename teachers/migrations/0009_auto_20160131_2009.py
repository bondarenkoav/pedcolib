# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import precise_bbcode.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0008_auto_20160131_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='_article_rendered',
            field=models.TextField(editable=False, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='article',
            field=precise_bbcode.fields.BBCodeTextField(no_rendered_field=True, verbose_name='Текст статьи', blank=True),
        ),
    ]
