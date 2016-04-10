# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust, ResizeToFill
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from autoslug import AutoSlugField

class Posts(models.Model):   #Должности
    class Meta:
        db_table = 'Posts'
        verbose_name = 'Должность'
        verbose_name_plural = 'Виды должностей'
    Name        = models.CharField(verbose_name='Должность',max_length=100)
    slug        = AutoSlugField(populate_from='Name')
    def __str__(self):
        return self.Name

class Ranks(models.Model):   #Звание
    class Meta:
        db_table = 'Ranks'
        verbose_name = 'Звание'
        verbose_name_plural = 'Виды званий'
    Name        = models.CharField(verbose_name='Звание',max_length=100)
    slug        = AutoSlugField(populate_from='Name')
    def __str__(self):
        return self.Name

class Degreys(models.Model):    #Степень
    class Meta:
        db_table = 'Degreys'
        verbose_name = 'Степень'
        verbose_name_plural = 'Виды степеней'
    Name        = models.CharField(verbose_name='Степень',max_length=100)
    slug        = AutoSlugField(populate_from='Name')
    def __str__(self):
        return self.Name

class categoryQval(models.Model):    #Категория квалификации
    class Meta:
        db_table = 'categoryQval'
        verbose_name = 'Категория квалификации'
        verbose_name_plural = 'Виды категорий квалификации'
    Name        = models.CharField(verbose_name='Категория квалификации',max_length=100)
    slug        = AutoSlugField(populate_from='Name')
    def __str__(self):
        return self.Name

class Subject(models.Model):
    class Meta:
        db_table = 'subject'
        verbose_name = 'Предмет '
        verbose_name_plural = 'Список предметов '
    Name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='Name')
    def __str__(self):
        return self.Name

class teacher(models.Model):
    class Meta:
        db_table = 'teacher'
        verbose_name = 'Персоналий'
        verbose_name_plural = 'Персоналии'
    #Фамилия Имя Отчество преподавателя
    fullname    = models.CharField(verbose_name='Фамилия Имя Отчество',max_length=100)
    alias       = AutoSlugField(populate_from='fullname')
    post        = models.ManyToManyField(Posts, verbose_name='Должность', blank=True)  #Должность
    rank        = models.ManyToManyField(Ranks, verbose_name='Звание',blank=True)  #Звание (типа заслуженый учитель России и т.д.)
    degree      = models.ForeignKey(Degreys,verbose_name='Степень')    #Степень
    categoryQval= models.ForeignKey(categoryQval, verbose_name='Категория')    #Категория
    subjects    = models.ManyToManyField(Subject, verbose_name='Предмет', blank=True)   #Предметы
    ImagePath   = ProcessedImageField(
        upload_to='static/main_image/teachers',
        processors=[ResizeToFill(200, 350)],
        format='JPEG',
        options={'quality': 100},
        verbose_name='Путь до изображения')
    article     = RichTextField(verbose_name='Текст статьи',blank=True)    #Статья
    author      = models.ForeignKey(User)
    publish_date= models.DateTimeField(verbose_name='Дата публикации',auto_now_add=True)
    def __str__(self):
         return self.fullname

#Фотоальбом
class teacher_photo_album(models.Model):
    teacher = models.ForeignKey(teacher, verbose_name='Альбом')
    title = models.CharField(u'Название фотографии', max_length=100)
    descript = models.CharField(u'Описание фотографии', max_length=300, blank=True)
    photo = ProcessedImageField(
        upload_to='static/main_image/teachers/photo_album/',
        processors=[ResizeToFit(600, 480)],
        format='JPEG',
        options={'quality': 100},
        verbose_name='Путь до изображения')
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = "Фотографии"
    def __str__(self):
        return self.title