# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Креативная группа', 'verbose_name_plural': 'Креативные группы', 'ordering': ['nameGroup']},
        ),
        migrations.RemoveField(
            model_name='group',
            name='tags',
        ),
        migrations.AddField(
            model_name='group',
            name='ImagePath',
            field=models.ImageField(upload_to='static/main_image/groups', blank=True, verbose_name='Главное фото группы'),
        ),
        migrations.AlterField(
            model_name='group',
            name='article',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='group',
            name='nameGroup',
            field=models.CharField(max_length=100),
        ),
    ]
