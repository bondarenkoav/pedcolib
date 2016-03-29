from django.contrib import admin
from teachers.models import teacher, Degreys, Ranks, Posts, categoryQval, Subject

class teacherAdmin(admin.ModelAdmin):
    fields = ['fullname','ImagePath','post','rank','degree','categoryQval','subjects','article','author']
    list_filter = ['publish_date']
    list_display = ['fullname', 'alias', 'publish_date', 'author']

class PostsAdmin(admin.ModelAdmin):
    list_display = ['Name', 'slug']

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['Name', 'slug']

class RanksAdmin(admin.ModelAdmin):
    list_display = ['Name', 'slug']

class DegreysAdmin(admin.ModelAdmin):
    list_display = ['Name', 'slug']

class categoryQvalAdmin(admin.ModelAdmin):
    list_display = ['Name', 'slug']

admin.site.register(teacher, teacherAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Ranks, RanksAdmin)
admin.site.register(Degreys, DegreysAdmin)
admin.site.register(categoryQval, categoryQvalAdmin)