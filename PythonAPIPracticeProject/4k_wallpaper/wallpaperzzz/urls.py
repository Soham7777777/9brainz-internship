"""
URL configuration for wallpaperzzz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from wallpaperapp.views import categories_view, delete_category, edit_category, add_category, images_view, settings_view, profile_view, delete_image, delete_size, add_image, edit_image, login_required
from .forms import LoginForm
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', profile_view, name="home"),

    path('categories', categories_view, name="categories"),
    path('delete-category', delete_category, name="delete_category"),
    path('edit-category', edit_category, name="edit_category"),
    path('add-category', add_category, name="add_category"),

    path('images', images_view, name="images"),
    path('delete-image', delete_image, name="delete_image"),
    path('add-image', add_image, name="add_image"),
    path('edit-image', edit_image, name="edit_image"),

    path('settings', settings_view, name="settings"),
    path('delete-size', delete_size, name="delete_size"),

    path('login', LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('change-password', login_required(PasswordChangeView.as_view(success_url='', template_name='change_password.html')), name='change_password'),
    
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('v2/', include('image2app.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
