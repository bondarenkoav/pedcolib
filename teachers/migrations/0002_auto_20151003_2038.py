# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoryQval',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('Name', models.CharField(max_length=20)),
                ('Description', models.TextField()),
            ],
            options={
                'db_table': 'categoryQval',
            },
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='likes',
        ),
        migrations.AddField(
            model_name='teacher',
            name='ImagePath',
            field=models.ImageField(default='', upload_to='', height_field=300, width_field=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='categoryQval',
            field=models.ForeignKey(default=1, to='teachers.categoryQval'),
            preserve_default=False,
        ),
    ]
