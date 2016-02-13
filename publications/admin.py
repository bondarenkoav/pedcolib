from django.contrib import admin
from publications.models import publics

class publicationAdmin(admin.ModelAdmin):
    fields = ['title','description','Image','article','author','link']
    list_filter = ['publish_date']
    list_display = ['title','description','author']

admin.site.register(publics, publicationAdmin)