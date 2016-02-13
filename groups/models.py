from django.contrib.auth.models import User
from django.db import models

class group(models.Model):
    class Meta:
        db_table = 'group'
    #������� ��� �������� �������������
    nameGroup   = models.CharField(max_length=20)

    #ImagePath   = models.ImageField(upload_to='static/main_image/groups') #������� �����������
    article     = models.TextField()    #������

    #SEO-���������
    tags        = models.CharField(max_length=50)
    author      = models.ForeignKey(User)
    publish_date= models.DateTimeField(auto_now_add=True)
    likes       = models.IntegerField(default=0)
    def __str__(self):
         return self.nameGroup