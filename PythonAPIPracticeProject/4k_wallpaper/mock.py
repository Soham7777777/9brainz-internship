import django
import os
from pathlib import Path
from django.core.files import File
import random


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wallpaperzzz.settings")
django.setup()


from wallpaperapp.models import ImageCategory, Image, ImageTags
from userapp.models import User

MOCK_IMAGES_DIR = 'mock_images'

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
categories = ["Nature", "Technology", "Abstract", "Portraits", "Urban Exploration"]
category_thumbnails_dir = os.path.join(MOCK_IMAGES_DIR, 'category_thumbnails')
wallpapers_dir = os.path.join(MOCK_IMAGES_DIR, 'wallpapers')
wallpaper_category_dirs = [os.path.join(wallpapers_dir, d) for d in os.listdir(wallpapers_dir) if os.path.isdir(os.path.join(wallpapers_dir, d))]


def main() -> None:
    User.objects.create_superuser(email="sohamjobanputra7@gmail.com", password="soham@123")

    categories_instances: list[ImageCategory] = []
    image_instances: list[Image] = []

    for idx, file in enumerate(os.listdir(category_thumbnails_dir)):
        file_path = os.path.join(category_thumbnails_dir, file)
        if os.path.isfile(file_path):
            with Path(file_path).open(mode="rb") as f:
                category_instance = ImageCategory(name=f"{categories[idx]}", thumbnail=File(f, file))
                category_instance.save()
                categories_instances.append(category_instance)

    for idx_i, wallpaper_category_dir in enumerate(wallpaper_category_dirs, start=1):
        for idx_j, file in enumerate(os.listdir(wallpaper_category_dir), start=1):
            file_path = os.path.join(wallpaper_category_dir, file)
            if os.path.isfile(file_path):
                with Path(file_path).open(mode="rb") as f:
                    image_instance = Image(image_file=File(f, file), category=categories_instances[idx_i - 1], download_count=random.randint(47, 67))
                    image_instance.save()
                    image_instances.append(image_instance)


    for image_instance in image_instances:
        random_number_of_tags = random.randint(3, 7)
        for _ in range(random_number_of_tags):
            ImageTags(image=image_instance, tag=random.choice(tags)).save()


if __name__ == '__main__':
    main()
