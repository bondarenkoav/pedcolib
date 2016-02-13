# -*- coding: utf-8 -*-

__author__ = 'ipman'

from django.forms import ModelForm
from graduates.models import graduate

class GraduateForm(ModelForm):
    class Meta:
        model = graduate
        fields = ['fullname', 'ImagePath', 'postandarea', 'article', 'soglasie']