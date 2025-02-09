from django.db import models
from django.core.validators import MinValueValidator


class WallpaperCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    thumbnail = models.ImageField(upload_to='category_thumbnails/')

    def __str__(self) -> str:
        return self.name


class Wallpaper(models.Model):
    category = models.ForeignKey(WallpaperCategory, related_name='wallpapers', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class WallpaperTag(models.Model):
    wallpaper = models.ForeignKey(Wallpaper, related_name='tags', on_delete=models.CASCADE)
    tag = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.tag


class ImageDimension(models.Model):
    width = models.IntegerField(validators=[MinValueValidator(1)])
    height = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self) -> str:
        return str(self.width) + 'x' + str(self.height)


class Image(models.Model):
    wallpaper = models.ForeignKey(Wallpaper, related_name='images', on_delete=models.CASCADE)
    image_file = models.ImageField(upload_to='images/')
    download_count = models.IntegerField(default=0)
    dimension = models.ForeignKey(ImageDimension, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id)


class SiteSettings(models.Model):
    max_image_size = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self) -> str:
        return str(self.max_image_size)
