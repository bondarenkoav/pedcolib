from django.contrib import admin

from graduates.models import graduate

class graduateAdmin(admin.ModelAdmin):
    fields = ['fullname','postandarea','ImagePath','article','soglasie','veryfid_data']
    list_filter = ['publish_date']
    list_display = ['fullname', 'publish_date', 'veryfid_data']

admin.site.register(graduate, graduateAdmin)