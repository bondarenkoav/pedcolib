# -*- coding: utf-8 -*-
__author__ = 'ipman'

from django.forms import ModelForm
from responses.models import response

class ResponsesForm(ModelForm):
     class Meta:
         model = response
         fields = ['title','name','article']