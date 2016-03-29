# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fvgallery', '0004_auto_20160226_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='link',
        ),
        migrations.AddField(
            model_name='video',
            name='video',
            field=embed_video.fields.EmbedVideoField(verbose_name='uСсылка на видео', default=''),
            preserve_default=False,
        ),
    ]
