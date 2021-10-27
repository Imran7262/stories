from django import forms

from .models import *


class cate(forms.ModelForm):
    class Meta:
        model=category
        fields='__all__'


class img(forms.ModelForm):
    class Meta:
        model=photos
        fields=('title','img','ctg','disc')

class for_astory(forms.ModelForm):
    class Meta:
        model=aply_for_story
        fields=('title','write')