from django import forms

from image2app.models import ImageDimension
from .models import ImageCategory, ImageSize, SiteSettings
from django.core.exceptions import ValidationError
from PIL import Image as PILImage
import re


def validate_name(value) -> None:
    if not re.match(r'^[A-Za-z]+( [A-Za-z]+)*$', value):
        raise ValidationError("Name should only contain English alphabets and spaces, with no spaces at the start or end.")


def validate_image_size(image) -> None:
    if image.size > 1024 * 1024:
        raise ValidationError("Image size should be 1MB or less.")


class SearchForm(forms.Form):
    query = forms.CharField(max_length=128, required=False, initial='')


class ImageCategoryForm(forms.ModelForm):
    name = forms.CharField(validators=[validate_name], max_length=255)
    thumbnail = forms.ImageField(validators=[validate_image_size])
    
    class Meta:
        model = ImageCategory
        fields = ['name', 'thumbnail']


class EditImageCategoryForm(forms.ModelForm):
    name = forms.CharField(validators=[validate_name], max_length=255, required=True)
    thumbnail = forms.ImageField(validators=[validate_image_size], required=False)
    
    class Meta:
        model = ImageCategory
        fields = ['name', 'thumbnail']


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = ['max_image_size', 'compress_image_on_save']
        


class ImageSizeForm(forms.ModelForm):
    class Meta:
        model = ImageDimension
        fields = ['width', 'height']
        widgets = {
            'width': forms.NumberInput(attrs={'placeholder': 'Width', 'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'placeholder': 'Height', 'class': 'form-control'}),
        }


class ImageForm(forms.Form):
    image_file = forms.ImageField()
    category = forms.ModelChoiceField(queryset=ImageCategory.objects.all())
    tags = forms.CharField()


    def clean_image_file(self):
        image = self.cleaned_data.get("image_files")
        site_settings = SiteSettings.objects.first()
        if not site_settings:
            raise ValidationError("Maximum image size limit is not set")

        if image.size > site_settings.max_image_size * 1024:
            raise ValidationError("Image size exceeds the allowed limit")

        img = PILImage.open(image)
        width, height = img.size

        valid_sizes = list(ImageSize.objects.values_list("width", "height"))
        if not valid_sizes:
            raise ValidationError("There are no sizes to match against")

        if (width, height) not in valid_sizes:
            raise ValidationError("Image does not match to any supported dimensions")

        return image


    def clean_tags(self):
        tags_value = self.cleaned_data.get("tags", "")
        tags = [tag.strip() for tag in tags_value.split(",") if tag.strip()]
        if not tags:
            raise ValidationError("At least one valid tag is required")

        if not all(tag.islower() and all(c.isalpha() or c.isspace() for c in tag) for tag in tags):
            raise ValidationError("Tags must only contain lowercase letters and spaces")

        return tags


