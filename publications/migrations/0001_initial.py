# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='publics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='Заголовок публикации', max_length=30)),
                ('description', models.TextField(verbose_name='Краткое описание')),
                ('Image', models.ImageField(upload_to='static/main_image/publications')),
                ('article', ckeditor.fields.RichTextField(verbose_name='Текст публикации')),
                ('publish_date', models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)),
                ('link', models.CharField(verbose_name='Ваше имя', max_length=30, blank=True)),
                ('author', models.ForeignKey(verbose_name='Автор', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'publics',
            },
        ),
    ]
