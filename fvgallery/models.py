# -*- coding: utf-8 -*-
from django.db import models
from PIL import Image
from imagekit.models.fields import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill
from embed_video.fields import EmbedVideoField

#Альбом с фотографиями
class Album(models.Model):
    title = models.CharField('uНазвание альбома', max_length=100)
    alias = models.SlugField('uАлиас альбома', max_length=100, unique=True)
    article = models.TextField('uОписание альбома')
    ImagePath = ProcessedImageField(
        upload_to='static/main_image/photo/album_image',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 100},
        verbose_name='Путь до изображения')
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
    photo = ProcessedImageField(
        upload_to='static/main_image/photo/images/',
        processors=[ResizeToFit(600, 480)],
        format='JPEG',
        options={'quality': 100},
        verbose_name='Путь до изображения')
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