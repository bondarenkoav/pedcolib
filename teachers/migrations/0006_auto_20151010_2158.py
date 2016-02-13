# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_auto_20151010_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='tags',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='ImagePath',
            field=models.ImageField(height_field=300, upload_to='', verbose_name='Заголовок комментария', blank=True, width_field=200),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='alias',
            field=models.CharField(verbose_name='Заголовок комментария', max_length=20),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='article',
            field=models.TextField(verbose_name='Текст статьи', blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='fullname',
            field=models.CharField(verbose_name='Заголовок комментария', max_length=80),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='publish_date',
            field=models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(max_length=30, verbose_name='Заголовок комментария', blank=True),
        ),
    ]
