import os
import re
import time
from django import forms
from .models import ImageDimension, WallpaperCategory
from wallpaperapp.models import SiteSettings
from django.core.exceptions import ValidationError
from PIL import Image as PILImage
from django.core.files.uploadedfile import UploadedFile


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


class CategoryForm(forms.Form):
    category = forms.ModelChoiceField(queryset=WallpaperCategory.objects.all(), required=False, empty_label='All Categories')


class PaginationForm(forms.Form):
    per_page_objects = forms.ChoiceField(choices=(("3", "3"), ("5", "5"), ("7", "7"), ("10", "10")), initial=3, required=False)


    def clean_per_page_objects(self):
        try:
            return int(self.cleaned_data['per_page_objects'])
        except ValueError:
            return 3

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


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.ImageField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class AddWallpaperForm(forms.Form):
    name = forms.CharField(validators=[validate_name], max_length=255)
    image_files = MultipleFileField()
    category = forms.ModelChoiceField(queryset=WallpaperCategory.objects.all())
    tags = forms.CharField(required=False)

    editing = False

    def clean_image_files(self) -> list[tuple[UploadedFile, tuple[int, int]]]:
        images = self.cleaned_data['image_files']

        image_data = []

        for image in images:
            site_settings = SiteSettings.objects.first()
            if not site_settings:
                raise ValidationError("Maximum image size limit is not set")

            if image.size > site_settings.max_image_size * 1024:
                raise ValidationError("Image size exceeds the allowed limit")

            img = PILImage.open(image)
            width, height = img.size

            valid_sizes = list(ImageDimension.objects.values_list("width", "height"))
            if not valid_sizes:
                raise ValidationError("There are no sizes to match against")

            if (width, height) in valid_sizes:
                ext = os.path.splitext(image.name)[1]
                image.name = f"image{''.join(str(time.time()).split('.'))}{ext}"
                image_data.append((image, (width, height)))
            
        if not any(image_data) and not self.editing:
            raise ValidationError("At least one valid image is needed")

        return image_data


    def clean_tags(self) -> list[str]:
        tags_value = self.cleaned_data.get("tags", "")
        tags = [tag.strip() for tag in tags_value.split(",") if tag.strip()]
        # if not all(tag.islower() and all(c.isalpha() or c.isspace() for c in tag) for tag in tags):
        #     raise ValidationError("Tags must only contain lowercase letters and spaces")
        return tags or []
