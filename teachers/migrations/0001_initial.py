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
            name='Degreys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=20)),
                ('Description', models.TextField()),
            ],
            options={
                'db_table': 'Degreys',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=20)),
                ('Description', models.TextField()),
            ],
            options={
                'db_table': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Ranks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=20)),
                ('Description', models.TextField()),
            ],
            options={
                'db_table': 'Ranks',
            },
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fullname', models.CharField(max_length=80)),
                ('subject', models.CharField(max_length=30)),
                ('article', models.TextField()),
                ('tags', models.CharField(max_length=50)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('degree', models.ForeignKey(to='teachers.Degreys')),
                ('post', models.ForeignKey(to='teachers.Posts')),
                ('rank', models.ForeignKey(to='teachers.Ranks')),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
    ]
