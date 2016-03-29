# -*- coding: utf-8 -*-
from django.db import models
from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill
from embed_video.fields import EmbedVideoField

#Альбом с фотографиями
class Album(models.Model):
    title = models.CharField('uНазвание альбома', max_length=100)
    alias = models.SlugField('uАлиас альбома', max_length=100, unique=True)
    article = models.TextField('uОписание альбома')
    image = models.ImageField('uИзображение альбома', upload_to='static/main_image/album')
    img_thumb = ImageSpecField([
        Adjust(contrast=1.2, sharpness=1.1),
        ResizeToFill(200, 200)], source='image',
        format='JPEG', options={'quality': 90}
    )
    class Meta:
        ordering = ['title']
        verbose_name = 'Фотоальбом'
        verbose_name_plural = 'Фотоальбомы'
    def __str__(self):
        return self.title

#Фотографии в альбоме
class Photo(models.Model):
    title = models.CharField('uНазвание фотографии', max_length=100)
    album = models.ForeignKey(Album, verbose_name='Альбом')
    photo = models.ImageField('uФото', upload_to='static/main_image/gallery')
    photo_thumb = ImageSpecField([
        Adjust(contrast=1.2, sharpness=1.1),
        ResizeToFit(100, 100)], source='photo',
        format='JPEG', options={'quality': 90}
    )
    photo_big = ImageSpecField([
        Adjust(contrast=1.2, sharpness=1.1),
        ResizeToFit(640, 480)], source='photo',
        format='JPEG', options={'quality': 90}
    )
    publish_date= models.DateTimeField(verbose_name='Дата добавления',auto_now_add=True)
    class Meta:
        ordering = ['title']
        verbose_name = 'Фото'
        verbose_name_plural = "Фотографии"
    def __str__(self):
        return self.title

#Видео
class Video(models.Model):
    title = models.CharField('Название видео', max_length=100)
    video = EmbedVideoField('Ссылка на видео')
    publish_date= models.DateTimeField('uДата добавления',auto_now_add=True)
    class Meta:
        ordering = ['-publish_date']
        verbose_name = 'Видео'
        verbose_name_plural = "Видеотека"
    def __str__(self):
        return self.title