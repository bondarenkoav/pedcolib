# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fvgallery', '0002_auto_20160225_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='img',
        ),
        migrations.RemoveField(
            model_name='album',
            name='slug',
        ),
        migrations.AddField(
            model_name='album',
            name='alias',
            field=models.SlugField(max_length=100, unique=True, default='', verbose_name='Алиас альбома'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(upload_to='images', default='', verbose_name='Изображение альбома'),
            preserve_default=False,
        ),
    ]
