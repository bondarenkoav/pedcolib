# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

class novosti(models.Model):
    class Meta:
        db_table = 'novosti'
    title       = models.CharField(max_length=100)
    ImagePath   = models.ImageField(upload_to='static/main_image/news',verbose_name="Изображение новости") #Главное изображение
    article     = RichTextField()
    author      = models.ForeignKey(User)
    publish_date= models.DateTimeField(auto_now_add=True)
    likes       = models.IntegerField(default=0)
    def __str__(self):
         return self.title