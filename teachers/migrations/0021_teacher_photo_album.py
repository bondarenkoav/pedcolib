# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0020_auto_20160409_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher_photo_album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Название фотографии')),
                ('descript', models.CharField(max_length=300, verbose_name='Описание фотографии')),
                ('photo', imagekit.models.fields.ProcessedImageField(verbose_name='Путь до изображения', upload_to='static/main_image/teachers/photo_album/')),
                ('teacher', models.ForeignKey(verbose_name='Альбом', to='teachers.teacher')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]
