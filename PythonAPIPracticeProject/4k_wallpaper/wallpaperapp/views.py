import time
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Count, Q, Sum
from django.conf import settings

from image2app.models import ImageDimension
from .forms import EditImageCategoryForm, ImageCategoryForm, ImageForm, ImageSizeForm, SearchForm, SiteSettingsForm
from .models import Image, ImageCategory, ImageSize, ImageTags, SiteSettings
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.core.files.storage import default_storage
import os


@login_required
def categories_view(request: HttpRequest) -> HttpResponse:
    form = SearchForm(request.GET)
    categories = ImageCategory.objects.all()
    
    if form.is_valid():
        query = form.cleaned_data.get('query', '').strip()
        if query:
            categories = categories.filter(name__icontains=query)
    
    categories = categories.annotate(image_count=Count('images'))
    categories = categories.values('name', 'thumbnail', 'image_count', 'id')
    
    return render(request, 'wallpaperapp/categories.html', {'form': form, 'categories': categories, "MEDIA_URL": settings.MEDIA_URL})
    

@login_required
def delete_category(request: HttpRequest) -> HttpResponse:
    category_id = request.GET.get('id')
    category = ImageCategory.objects.filter(id=category_id).first()
    
    if category:
        name = category.name
        category.delete()
        messages.success(request, f"Category {name} has been deleted")
    else:
        messages.info(request, "category does not exist")
    
    return redirect('categories')


@login_required
def add_category(request: HttpRequest) -> HttpResponse:
    form = ImageCategoryForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            timestamped_name = '-'.join(category.name.split()) + category.thumbnail.name[category.thumbnail.name.rfind('.'):]
            file_path = default_storage.save(os.path.join('category_thumbnails', timestamped_name), category.thumbnail)
            category.thumbnail.name = file_path
            category.save()
            messages.success(request, f"new category '{form.cleaned_data['name']}' is added")
            return redirect('categories')
    else:
        form = ImageCategoryForm()

    return render(request, 'wallpaperapp/add_category.html', {'form': form})


@login_required
def edit_category(request: HttpRequest) -> HttpResponse:
    category_id = request.GET.get('id')
    category = get_object_or_404(ImageCategory, id=category_id)  
    if request.method == 'POST':
        form = EditImageCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.info(request, f"Category '{form.cleaned_data['name']}' has been edited")
            return redirect('categories')
    else:
        form = EditImageCategoryForm(instance=category)
    return render(request, 'wallpaperapp/edit_category.html', {'form': form, 'category': category})


@login_required
def images_view(request: HttpRequest) -> HttpResponse:
    form = SearchForm(request.GET)
    images = Image.objects.all()
    
    if form.is_valid():
        query = form.cleaned_data.get('query', '').strip()
        if query:
            images = images.filter(
                Q(tags__tag__icontains=query) |
                Q(category__name__icontains=query)
            ).distinct()
    
    image_data = []
    for image in images.values('image_file', 'download_count', 'category__name', 'id'):
        tags = list(ImageTags.objects.filter(image_id=image['id']).values_list('tag', flat=True))
        image_name = image['image_file'].split('/')[-1]
        image_data.append({**image, 'tags': tags, 'name': image_name})

    return render(request, 'wallpaperapp/images.html', {'form': form, 'images': image_data, 'MEDIA_URL': settings.MEDIA_URL})


@login_required
def settings_view(request: HttpRequest) -> HttpResponse:
    try:
        site_settings = SiteSettings.objects.first()
    except SiteSettings.DoesNotExist:
        site_settings = None

    form1 = SiteSettingsForm(instance=site_settings)

    if request.method == 'POST':
        if 'form1_submit' in request.POST:
            form1 = SiteSettingsForm(request.POST, instance=site_settings)
            if form1.is_valid():
                form1.save()

        elif 'form2_submit' in request.POST:
            form2 = ImageSizeForm(request.POST)
            if form2.is_valid():
                form2.save()

    sizes = ImageDimension.objects.all()
    return render(request, 'wallpaperapp/settings.html', {'form1': form1, "form2": ImageSizeForm(), "sizes": sizes, "password_change_form": PasswordChangeForm(request.user)})


@login_required
def profile_view(request: HttpRequest) -> HttpResponse:
    user = request.user
    total_categories = ImageCategory.objects.count()
    total_images = Image.objects.count()
    total_downloads = Image.objects.aggregate(Sum('download_count'))['download_count__sum'] or 0

    context = {
        'email': user.email,
        'total_categories': total_categories,
        'total_images': total_images,
        'total_downloads': total_downloads
    }

    return render(request, 'wallpaperapp/profile.html', {"context": context})


@login_required
def delete_image(request: HttpRequest) -> HttpResponse:
    image_id = request.GET.get('id')
    image = Image.objects.filter(id=image_id).first()
    
    if image:
        name = image.image_file.name.split('/')[-1]
        image.delete()
        messages.success(request, f"Image {name} has been deleted")
    else:
        messages.info(request, "image does not exist")
    
    return redirect('images')


@login_required
def delete_size(request: HttpRequest) -> HttpResponse:
    size_id = request.GET.get('id')
    size = ImageDimension.objects.filter(id=size_id).first()

    if size:
        size.delete()
    else:
        messages.info(request, "size does not exist")
    
    return redirect("settings")


@login_required
def add_image(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.cleaned_data["image_file"]
            ext = os.path.splitext(image_file.name)[1]
            image_file.name = f"image{''.join(str(time.time()).split('.'))}{ext}"

            image = Image.objects.create(
                category=form.cleaned_data["category"],
                image_file=image_file
            )

            new_tags = set(form.cleaned_data["tags"])
            ImageTags.objects.bulk_create(
                [ImageTags(image=image, tag=tag) for tag in new_tags]
            )

            messages.success(request, f"Image {image.image_file.name.split('/')[-1]} added successfully")
            return redirect("images")
    else:
        form = ImageForm()

    return render(request, "wallpaperapp/add_image.html", {"form": form})


@login_required
def edit_image(request: HttpRequest) -> HttpResponse:
    image_id = request.GET.get("id")
    image = get_object_or_404(Image, id=image_id)

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            if "image_file" in request.FILES:
                image_file = form.cleaned_data["image_file"]
                ext = os.path.splitext(image_file.name)[1]
                image_file.name = f"image{''.join(str(time.time()).split('.'))}{ext}"
                image.image_file = image_file

            image.category = form.cleaned_data["category"]
            image.save()

            image.tags.all().delete()
            new_tags = set(form.cleaned_data["tags"])
            ImageTags.objects.bulk_create(
                [ImageTags(image=image, tag=tag) for tag in new_tags]
            )

            messages.success(request, "Image updated successfully")
            return redirect("images")
    else:
        initial_data = {
            "category": image.category,
            "tags": ", ".join(image.tags.values_list("tag", flat=True)),
        }
        form = ImageForm(initial=initial_data)

    return render(request, "wallpaperapp/edit_image.html", {"form": form, "image": image, 'MEDIA_URL': settings.MEDIA_URL})
