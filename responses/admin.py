from django.contrib import admin
from responses.models import response

class responseAdmin(admin.ModelAdmin):
    fields = ['name','title','article','veryfid_data']
    list_filter = ['publish_date']
    list_display = ['name','title','publish_date','veryfid_data']

admin.site.register(response,responseAdmin)
