# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill
from imagekit.models import ProcessedImageField

class Slider(models.Model):
    title = models.CharField(verbose_name='Имя изображения', max_length=100)
    ImagePath_resize = ProcessedImageField(
        upload_to='static/main_image/slider',
        processors=[ResizeToFill(750, 350)],
        format='JPEG',
        options={'quality': 100},
        verbose_name='Путь до изображения'
    )
    description= models.TextField(verbose_name='Описание', blank=True)
    link       = models.CharField(verbose_name='Ссылка на страницу', max_length=100, blank=True)
    def __str__(self):
            return self.title
    class Meta:
        db_table = 'Slider'
        ordering = ['title']
        verbose_name = 'Слайд'
        verbose_name_plural = "Слайды"
