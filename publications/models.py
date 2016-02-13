# -*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class publics(models.Model):
    class Meta:
        db_table = 'publics'
    title        = models.CharField(verbose_name='Заголовок публикации', max_length=30)
    description  = models.TextField(verbose_name='Краткое описание')
    Image        = models.ImageField(upload_to='static/main_image/publications') #Главное изображение
    article      = RichTextField(verbose_name='Текст публикации')
    author       = models.ForeignKey(User,verbose_name='Автор')
    publish_date = models.DateTimeField(verbose_name='Дата публикации',auto_now_add=True)
    link         = models.CharField(verbose_name='Ссылка на источник', max_length=30, blank=True)
    def __str__(self):
        return self.title