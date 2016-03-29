# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0016_auto_20160306_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='name',
            new_name='Name',
        ),
        migrations.RemoveField(
            model_name='categoryqval',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='degreys',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='ranks',
            name='Description',
        ),
        migrations.AddField(
            model_name='categoryqval',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='Name', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='degreys',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='Name', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='Name', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ranks',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='Name', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='Name', default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='categoryQval',
            field=models.ForeignKey(verbose_name='Категория', to='teachers.categoryQval'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='degree',
            field=models.ForeignKey(verbose_name='Степень', to='teachers.Degreys'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='post',
            field=models.ManyToManyField(verbose_name='Должность', to='teachers.Posts', blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='rank',
            field=models.ManyToManyField(verbose_name='Звание', to='teachers.Ranks', blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(verbose_name='Предмет', to='teachers.Subject', blank=True),
        ),
    ]
