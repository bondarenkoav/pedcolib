# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Slider(models.Model):
    class Meta:
        db_table = 'Slider'
    ImagePath  = models.ImageField(upload_to='static/main_image/slider',verbose_name='Путь до изображения')
    title      = models.CharField(verbose_name='Имя изображения', max_length=100)
    description= models.TextField(verbose_name='Описание')
    link       = models.CharField(verbose_name='Ссылка на страницу', max_length=100)
    def __str__(self):
         return self.title