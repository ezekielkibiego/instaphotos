from django import forms
from django.db.models import fields
from instaapp.models import Image,Profile

class PicImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={

        'id': 'image1', 'class': 'images2'

    }))

    class Meta:
        model = Image
        fields = ['photo_name','photo_caption','image']

