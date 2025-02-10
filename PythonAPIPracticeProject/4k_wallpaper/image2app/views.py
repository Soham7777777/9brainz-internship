from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Image, Wallpaper, WallpaperCategory, SiteSettings, ImageDimension, WallpaperTag
from .forms import EditImageCategoryForm, ImageCategoryForm, SearchForm, SiteSettingsForm, ImageSizeForm, AddWallpaperForm
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Sum, Q
from django.conf import settings
from django.core.files.storage import default_storage
import os
from django.contrib import messages


@login_required
def profile_view(request: HttpRequest) -> HttpResponse:
    user = request.user
    total_categories = WallpaperCategory.objects.count()
    total_images = Image.objects.count()
    total_downloads = Image.objects.aggregate(Sum('download_count'))['download_count__sum'] or 0

    context = {
        'email': user.email,
        'total_categories': total_categories,
        'total_images': total_images,
        'total_downloads': total_downloads
    }

    return render(request, 'image2app/profile.html', {"context": context})


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
    return render(request, 'image2app/settings.html', {'form1': form1, "form2": ImageSizeForm(), "sizes": sizes, "password_change_form": PasswordChangeForm(request.user)})


@login_required
def delete_size(request: HttpRequest) -> HttpResponse:
    size_id = request.GET.get('id')
    size = ImageDimension.objects.filter(id=size_id).first()

    if size:
        size.delete()
    else:
        messages.info(request, "size does not exist")
    
    return redirect("v2_settings")


@login_required
def categories_view(request: HttpRequest) -> HttpResponse:
    form = SearchForm(request.GET)
    categories = WallpaperCategory.objects.all()
    
    if form.is_valid():
        query = form.cleaned_data.get('query', '').strip()
        if query:
            categories = categories.filter(name__icontains=query)
    
    # categories = categories.annotate(image_count=Count('images'))
    # categories = categories.values('name', 'thumbnail', 'image_count', 'id')
    categories = categories.values('name', 'thumbnail', 'id')
    
    return render(request, 'image2app/categories.html', {'form': form, 'categories': categories, "MEDIA_URL": settings.MEDIA_URL})
    

@login_required
def delete_category(request: HttpRequest) -> HttpResponse:
    category_id = request.GET.get('id')
    category = WallpaperCategory.objects.filter(id=category_id).first()
    
    if category:
        name = category.name
        category.delete()
        messages.success(request, f"Category {name} has been deleted")
    else:
        messages.info(request, "category does not exist")
    
    return redirect('v2_categories')


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
            return redirect('v2_categories')
    else:
        form = ImageCategoryForm()

    return render(request, 'image2app/add_category.html', {'form': form})


@login_required
def edit_category(request: HttpRequest) -> HttpResponse:
    category_id = request.GET.get('id')
    category = get_object_or_404(WallpaperCategory, id=category_id)  
    if request.method == 'POST':
        form = EditImageCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.info(request, f"Category '{form.cleaned_data['name']}' has been edited")
            return redirect('v2_categories')
    else:
        form = EditImageCategoryForm(instance=category)
    return render(request, 'image2app/edit_category.html', {'form': form, 'category': category})


@login_required
def wallpapers_view(request: HttpRequest) -> HttpResponse:
    form = SearchForm(request.GET)

    wallpapers_data = []
    wallpapers = Wallpaper.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query', '').strip()
        if query:
            wallpapers = wallpapers.filter(
                Q(name__icontains=query) |
                Q(tags__tag__icontains=query) |
                Q(category__name__icontains=query)
            ).distinct()

    for wallpaper in wallpapers.values('name', 'category', 'id'):
        tags = list(WallpaperTag.objects.filter(wallpaper_id=wallpaper['id']).values_list('tag', flat=True))
        category = str(WallpaperCategory.objects.filter(id=wallpaper['category']).first())
        wallpapers_data.append({**wallpaper, 'tags': tags, 'category': category})
    
    return render(request, 'image2app/wallpapers.html', {'wallpapers': wallpapers_data, 'form': form})


@login_required
def add_wallpaper(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = AddWallpaperForm(request.POST, request.FILES)
        if form.is_valid():
            images = form.cleaned_data["image_files"]

            wallpaper = Wallpaper(category=WallpaperCategory.objects.filter(name=form.cleaned_data["category"]).first(), name=form.cleaned_data["name"])
            wallpaper.save()

            for tag in form.cleaned_data["tags"]:
                WallpaperTag(wallpaper=wallpaper, tag=tag).save()
            
            for image in images:
                Image(wallpaper=wallpaper, image_file=image[0], dimension=ImageDimension.objects.filter(width=image[1][0], height=image[1][1]).first()).save()
            
            messages.success(request, f"Wallpaper {wallpaper.name} added successfully")
            return redirect("wallpapers")

    else:
        form = AddWallpaperForm()

    return render(request, 'image2app/add_wallpaper.html', {"form": form, "sizes": ImageDimension.objects.all()})


@login_required
def delete_wallpaper(request: HttpRequest) -> HttpResponse:
    wallpaper_id = request.GET.get('id')
    wallpaper = Wallpaper.objects.filter(id=wallpaper_id).first()

    if wallpaper:
        name = str(wallpaper)
        wallpaper.delete()
        messages.success(request, f"Wallpaper {name} has been deleted")
    else:
        messages.info(request, "wallpaper does not exist")
    
    return redirect('wallpapers')


