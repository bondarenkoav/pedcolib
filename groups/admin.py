from django.contrib import admin

from groups.models import group

class groupsAdmin(admin.ModelAdmin):
    fields = ['nameGroup', 'tags', 'author', 'article']
    list_filter = ['publish_date']
    list_display = ['nameGroup', 'publish_date', 'author']

admin.site.register(group, groupsAdmin)