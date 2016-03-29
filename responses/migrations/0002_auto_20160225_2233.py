# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('responses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='response',
            options={'verbose_name_plural': 'Отзывы', 'ordering': ['-publish_date'], 'verbose_name': 'Отзыв'},
        ),
        migrations.AlterField(
            model_name='response',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок комментария'),
        ),
    ]
