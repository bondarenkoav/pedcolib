# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

class graduate(models.Model):
    class Meta:
        db_table = 'graduate'

    fullname     = models.CharField(verbose_name='Ваше ФИО', max_length=80, blank=True)
    postandarea  = models.TextField(verbose_name='Где и кем работаете', blank=True)
    ImagePath    = models.ImageField(upload_to='static/main_image/graduates', verbose_name='Ваше фото', blank=True) #Главное изображение
    article      = models.TextField(verbose_name='Несколько слов о себе',)    #Статья
    publish_date = models.DateTimeField(auto_now_add=True)
    soglasie     = models.BooleanField(verbose_name='Даю согласие на обработку личных данных',)
    veryfid_data = models.BooleanField(verbose_name='Данные подтверждены администратором сайта', default=False)

    def __str__(self):
         return self.fullname