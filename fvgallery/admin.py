from django.contrib import admin
from .models import Album, Photo, Video
from embed_video.admin import AdminVideoMixin

class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Video,VideoAdmin)