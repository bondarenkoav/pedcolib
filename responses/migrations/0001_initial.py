# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок комментария')),
                ('name', models.CharField(max_length=30, verbose_name='Ваше имя')),
                ('article', ckeditor.fields.RichTextField(verbose_name='Текст отзыва')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('veryfid_data', models.BooleanField(default=False, verbose_name='Данные подтверждены администратором сайта')),
            ],
            options={
                'db_table': 'response',
            },
        ),
    ]
