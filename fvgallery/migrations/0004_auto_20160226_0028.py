# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fvgallery', '0003_auto_20160225_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='article',
            field=models.TextField(verbose_name='uОписание альбома', default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='alias',
            field=models.SlugField(verbose_name='uАлиас альбома', unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(upload_to='static/main_image/album', verbose_name='uИзображение альбома'),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(verbose_name='uНазвание альбома', max_length=100),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='static/main_image/gallery', verbose_name='uФото'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(verbose_name='uНазвание фотографии', max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='link',
            field=models.CharField(verbose_name='uСсылка на видео', max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='uДата добавления'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(verbose_name='uНазвание видео', max_length=100),
        ),
    ]
