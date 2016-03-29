# -*- coding: utf-8 -*-

__author__ = 'ipman'

from django.forms import ModelForm
from graduates.models import graduate
from captcha.fields import CaptchaField

class GraduateForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = graduate
        fields = ['fullname', 'ImagePath', 'postandarea', 'article', 'soglasie']