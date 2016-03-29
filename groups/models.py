# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

class group(models.Model):
    nameGroup   = models.CharField(max_length=100)   #Фамилия Имя Отчество преподавателя
    ImagePath   = models.ImageField(upload_to='static/main_image/groups',verbose_name='Главное фото группы', blank=True) #Главное изображение
    article     = RichTextField(verbose_name='Текст статьи',blank=True)    #Статья
    #tags        = models.CharField(max_length=100)
    author      = models.ForeignKey(User)
    publish_date= models.DateTimeField(auto_now_add=True)
    likes       = models.IntegerField(default=0)
    class Meta:
        db_table = 'group'
        ordering = ['nameGroup']
        verbose_name = "Креативная группа"
        verbose_name_plural = "Креативные группы"
        def __unicode__(self):
            return self.title