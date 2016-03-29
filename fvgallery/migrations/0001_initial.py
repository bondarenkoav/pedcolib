# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название альбома', max_length=100)),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка для альбома', max_length=100)),
                ('img', models.ImageField(help_text='Размер изображения 200px на 200px', verbose_name='Изображение альбома', upload_to='images')),
            ],
            options={
                'verbose_name_plural': 'Фотоальбомы',
                'ordering': ['title'],
                'verbose_name': 'Фотоальбом',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название фотографии', max_length=100)),
                ('img', models.ImageField(help_text='Желательно, чтоб фото было не большого размера', verbose_name='Фото', upload_to='images')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('album', models.ForeignKey(to='fvgallery.Album', verbose_name='Альбом')),
            ],
            options={
                'verbose_name_plural': 'Фотографии',
                'ordering': ['title'],
                'verbose_name': 'Фото',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название видео', max_length=100)),
                ('link', models.CharField(verbose_name='Ссылка на видео', max_length=100)),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name_plural': 'Видеотека',
                'ordering': ['-publish_date'],
                'verbose_name': 'Видео',
            },
        ),
    ]
