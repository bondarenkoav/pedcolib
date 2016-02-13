from django.forms import ModelForm
from django.contrib import admin
from news.models import novosti

class novostiAdmin(admin.ModelAdmin):
    fields = ['title','article','ImagePath','author']
    list_filter = ['publish_date']
    list_display = ['title', 'publish_date', 'author']

admin.site.register(novosti, novostiAdmin)