# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField

class response(models.Model):
    class Meta:
        db_table = 'response'
    title        = models.CharField(verbose_name='Заголовок комментария', max_length=100)
    name         = models.CharField(verbose_name='Ваше имя', max_length=30)
    article      = RichTextField(verbose_name='Текст отзыва')
    publish_date = models.DateTimeField(verbose_name='Дата публикации',auto_now_add=True)
    veryfid_data = models.BooleanField(verbose_name='Данные подтверждены администратором сайта',default=False)
    def __str__(self):
         return self.title