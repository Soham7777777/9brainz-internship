import re
from django import forms
from .models import ImageDimension, SiteSettings, WallpaperCategory
from django.core.exceptions import ValidationError


def validate_name(value):
    if not re.match(r'^[A-Za-z]+( [A-Za-z]+)*$', value):
        raise ValidationError("Name should only contain English alphabets and spaces, with no spaces at the start or end.")


def validate_category_thumbnail_size(image):
    if image.size > 1024 * 1024:
        raise ValidationError("Image size should be 1MB or less.")


class ImageSizeForm(forms.ModelForm):
    class Meta:
        model = ImageDimension
        fields = ['width', 'height']
        widgets = {
            'width': forms.NumberInput(attrs={'placeholder': 'Width', 'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'placeholder': 'Height', 'class': 'form-control'}),
        }


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = ['max_image_size']
        widgets = {
            'max_image_size': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'})
        }


class SearchForm(forms.Form):
    query = forms.CharField(max_length=128, required=False, initial='')


class ImageCategoryForm(forms.ModelForm):
    name = forms.CharField(validators=[validate_name], max_length=255)
    thumbnail = forms.ImageField(validators=[validate_category_thumbnail_size])
    
    class Meta:
        model = WallpaperCategory
        fields = ['name', 'thumbnail']


class EditImageCategoryForm(forms.ModelForm):
    name = forms.CharField(validators=[validate_name], max_length=255, required=True)
    thumbnail = forms.ImageField(validators=[validate_category_thumbnail_size], required=False)
    
    class Meta:
        model = WallpaperCategory
        fields = ['name', 'thumbnail']
