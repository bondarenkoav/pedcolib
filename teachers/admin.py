from django.contrib import admin
from teachers.models import teacher, Degreys, Ranks, Posts, categoryQval

class teacherAdmin(admin.ModelAdmin):
    fields = ['fullname','alias','ImagePath','post','rank','degree','categoryQval','subject','article']
    list_filter = ['publish_date']
    list_display = ['fullname', 'post', 'publish_date', 'author']

admin.site.register(teacher, teacherAdmin)
admin.site.register(Posts)
admin.site.register(Ranks)
admin.site.register(Degreys)
admin.site.register(categoryQval)