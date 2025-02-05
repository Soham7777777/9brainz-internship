from django.db import models
from django.core.validators import MinValueValidator

class ImageCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    thumbnail = models.ImageField(upload_to='category_thumbnails/')

    def __str__(self) -> str:
        return self.name


class ImageTags(models.Model):
    image = models.ForeignKey('Image', related_name='tags', on_delete=models.CASCADE)
    tag = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.tag


class Image(models.Model):
    category = models.ForeignKey(ImageCategory, related_name='images', on_delete=models.CASCADE)
    image_file = models.ImageField(upload_to='images/')
    download_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.id


class ImageSize(models.Model):
    width = models.IntegerField(validators=[MinValueValidator(1)])
    height = models.IntegerField(validators=[MinValueValidator(1)])


class SiteSettings(models.Model):
    max_image_size = models.IntegerField(validators=[MinValueValidator(1)])
