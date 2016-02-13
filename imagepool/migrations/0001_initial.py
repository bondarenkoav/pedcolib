# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePool',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('uploaded', models.DateTimeField(verbose_name='Выгружен', auto_now_add=True, db_index=True)),
                ('image', models.ImageField(verbose_name='Изображение', upload_to='imagepool/%Y/%m')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'изображения',
                'verbose_name': 'изображение',
                'ordering': ['user', '-uploaded'],
            },
        ),
    ]
