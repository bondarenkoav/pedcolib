from django.contrib import admin
from home.models import Slider

class SliderAdmin(admin.ModelAdmin):
    fields      = ['title','description','link','ImagePath']
    list_display= ['title','description']

admin.site.register(Slider, SliderAdmin)