from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Image, WallpaperCategory, SiteSettings, ImageDimension
from .forms import EditImageCategoryForm, ImageCategoryForm, SearchForm, SiteSettingsForm, ImageSizeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Sum
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
