# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('graduates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='graduate',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=20)),
                ('middlename', models.CharField(max_length=30, blank=True)),
                ('article', models.TextField()),
                ('tags', models.CharField(max_length=50, blank=True)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'graduate',
            },
        ),
        migrations.RemoveField(
            model_name='graduates',
            name='author',
        ),
        migrations.DeleteModel(
            name='graduates',
        ),
    ]
