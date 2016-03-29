# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill
from imagekit.models import ProcessedImageField

class graduate(models.Model):
    fullname     = models.CharField(verbose_name='Ваше ФИО', max_length=80, blank=True)
    postandarea  = ProcessedImageField(
        upload_to='static/main_image/graduates',
        processors=[ResizeToFill(300, 400)],
        format='JPEG',
        options={'quality': 100},
        verbose_name='Ваше фото'
    )
    article      = models.TextField(verbose_name='Несколько слов о себе',)    #Статья
    publish_date = models.DateTimeField(auto_now_add=True)
    soglasie     = models.BooleanField(verbose_name='Даю согласие на обработку личных данных',)
    veryfid_data = models.BooleanField(verbose_name='Данные подтверждены администратором сайта', default=False)
    class Meta:
        db_table = 'graduate'
        ordering = ['fullname']
        verbose_name = 'Выпускник'
        verbose_name_plural = "Выпускники"
        def __unicode__(self):
            return self.title