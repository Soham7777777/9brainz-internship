import django
import os
from pathlib import Path
from django.core.files import File
import random


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wallpaperzzz.settings")
django.setup()


from image2app.models import Wallpaper, WallpaperCategory, WallpaperTag, Image, ImageDimension
from userapp.models import User

MOCK_IMAGES_DIR = 'mock_images/wallpapers'

tags = [
    "nature", "landscape", "sunset", "mountains", "beach", "forest", "ocean", 
    "cityscape", "abstract", "minimalist", "sky", "clouds", "water", "autumn", 
    "spring", "winter", "summer", "night", "stars", "space", "flowers", "animals", 
    "wildlife", "architecture", "urban", "vintage", "retro", "technology", 
    "patterns", "art", "colorful", "dark", "black and white", "retro", "fog", 
    "desert", "tropical", "snow", "rain", "mountain range", "sunrise", "countryside", 
    "peaceful", "serene", "storm", "cloudy", "blue", "green", "pink", "red", 
    "purple", "yellow", "orange", "greenery", "sunbeam", "starry", "underwater"
]


def main() -> None:
    User.objects.create_superuser(email="sohamjobanputra7@gmail.com", password="soham@123")

    size1 = ImageDimension(width=3840, height=2160)
    size2 = ImageDimension(width=1920, height=1080)
    size3 = ImageDimension(width=1280, height=720)
    size1.save()
    size2.save()
    size3.save()


    thumbnail1_path = os.path.join(MOCK_IMAGES_DIR, 'Category1', 'thumbnail.png')
    thumbnail2_path = os.path.join(MOCK_IMAGES_DIR, 'Category2', 'thumbnail.png')
    thumbnail3_path = os.path.join(MOCK_IMAGES_DIR, 'Category3', 'thumbnail.png')


    category1 = WallpaperCategory(name="Nature", thumbnail=File(Path(thumbnail1_path).open(mode="rb")))
    category2 = WallpaperCategory(name="Technology", thumbnail=File(Path(thumbnail2_path).open(mode="rb")))
    category3 = WallpaperCategory(name="Portraits", thumbnail=File(Path(thumbnail3_path).open(mode="rb")))
    category1.save()
    category2.save()
    category3.save()


    wallpapers = [
        Wallpaper(category=category1, name="Mountain"),
        Wallpaper(category=category1, name="Sea"),
        Wallpaper(category=category1, name="Land"),

        Wallpaper(category=category2, name="Mountain"),
        Wallpaper(category=category2, name="Sea"),
        Wallpaper(category=category2, name="Land"),

        Wallpaper(category=category3, name="Mountain"),
        Wallpaper(category=category3, name="Sea"),
        Wallpaper(category=category3, name="Land"),
    ]

    for wallpaper in wallpapers:
        wallpaper.save()


    for wallpaper in wallpapers:
        for _ in range(random.randint(5, 8)):
            WallpaperTag(wallpaper=wallpaper, tag=random.choice(tags)).save()
    

    image_paths = [
        os.path.join(MOCK_IMAGES_DIR, 'Category1', 'Wallpaper1', 'size1.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category1', 'Wallpaper1', 'size2.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category1', 'Wallpaper1', 'size3.png'),
        
        os.path.join(MOCK_IMAGES_DIR, 'Category1', 'Wallpaper2', 'size1.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category1', 'Wallpaper2', 'size2.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category1', 'Wallpaper2', 'size3.png'),

        os.path.join(MOCK_IMAGES_DIR, 'Category1', 'Wallpaper3', 'size1.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category1', 'Wallpaper3', 'size1.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category1', 'Wallpaper3', 'size1.png'),


        os.path.join(MOCK_IMAGES_DIR, 'Category2', 'Wallpaper1', 'size1.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category2', 'Wallpaper1', 'size2.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category2', 'Wallpaper1', 'size3.png'),
        
        os.path.join(MOCK_IMAGES_DIR, 'Category2', 'Wallpaper2', 'size1.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category2', 'Wallpaper2', 'size2.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category2', 'Wallpaper2', 'size3.png'),

        os.path.join(MOCK_IMAGES_DIR, 'Category2', 'Wallpaper3', 'size1.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category2', 'Wallpaper3', 'size1.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category2', 'Wallpaper3', 'size1.png'),


        os.path.join(MOCK_IMAGES_DIR, 'Category3', 'Wallpaper1', 'size1.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category3', 'Wallpaper1', 'size2.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category3', 'Wallpaper1', 'size3.png'),

        os.path.join(MOCK_IMAGES_DIR, 'Category3', 'Wallpaper2', 'size1.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category3', 'Wallpaper2', 'size2.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category3', 'Wallpaper2', 'size3.png'),

        os.path.join(MOCK_IMAGES_DIR, 'Category3', 'Wallpaper3', 'size1.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category3', 'Wallpaper3', 'size1.png'),
        os.path.join(MOCK_IMAGES_DIR, 'Category3', 'Wallpaper3', 'size1.png'),
    ]

    i = 0
    for wallpaper in wallpapers:
        for dimension in [size1, size2, size3]:
            Image(wallpaper=wallpaper, dimension=dimension, image_file=File(Path(image_paths[i]).open(mode="rb"))).save()
            i += 1


if __name__ == '__main__':
    main()
