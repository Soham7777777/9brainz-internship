import os
from django.db import models
from django.dispatch import receiver
from django.core.validators import MinValueValidator
from typing import Any
from wallpaperapp.models import SiteSettings as ImageSettings
from PIL import Image as ImageTools
from django_stubs_ext.db.models import TypedModelMeta
from django.core.exceptions import ObjectDoesNotExist


IS_SOFT = False


class WallpaperCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    thumbnail = models.ImageField(upload_to='category_thumbnails/')

    def __str__(self) -> str:
        return self.name


class Wallpaper(models.Model):
    category = models.ForeignKey(WallpaperCategory, related_name='wallpapers', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='wallpapers_thumbnails/', null=True, default=None)
    uploaded_at = models.DateTimeField(auto_now=True)

    class Meta(TypedModelMeta):
        ordering = ["uploaded_at"]

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
    dimension = models.ForeignKey(ImageDimension, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return str(self.id)


class SiteSettings(models.Model):
    max_image_size = models.IntegerField(validators=[MinValueValidator(1)])
    # compress_when_saved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.max_image_size)


@receiver(models.signals.post_delete, sender=WallpaperCategory)
def delete_wallpaper_category_thumbnail(sender, instance: WallpaperCategory, **kwargs: Any) -> None: # type: ignore
    if instance.thumbnail:
        if os.path.isfile(instance.thumbnail.path):
            os.remove(instance.thumbnail.path)


@receiver(models.signals.post_delete, sender=Wallpaper)
def delete_wallpaper_thumbnail(sender, instance: Wallpaper, **kwargs: Any) -> None: # type: ignore
    if instance.thumbnail:
        if os.path.isfile(instance.thumbnail.path):
            os.remove(instance.thumbnail.path)


@receiver(models.signals.post_delete, sender=Image)
def delete_image_files_and_delete_wallpaper_without_images(sender, instance: Image, **kwargs: Any) -> None: # type: ignore
    if instance.image_file:
        if os.path.isfile(instance.image_file.path):
            os.remove(instance.image_file.path)
    
    try:
        if not len(Image.objects.filter(wallpaper=instance.wallpaper).all()):
            instance.wallpaper.delete()
    except ObjectDoesNotExist:
        pass

@receiver(models.signals.post_save, sender=Image)
def compress_image(sender, instance: Image, **kwargs: Any) -> None: # type: ignore
    image_settings = ImageSettings.objects.all().first()

    if image_settings and image_settings.compress_image_on_save:
        with ImageTools.open(instance.image_file.path) as img:
            img.save(instance.image_file.path, optimize=True, quality=20)


@receiver(models.signals.pre_delete, sender=ImageDimension)
def delete_image_files_on_size_delete(sender, instance: ImageDimension, **kwargs: Any) -> None: # type: ignore
    if not IS_SOFT:
        Image.objects.filter(dimension=instance).all().delete()

