from django.urls import path 
from .views import add_category, categories_view, delete_category, edit_category, profile_view, settings_view, delete_size, wallpapers_view, delete_wallpaper, add_wallpaper


urlpatterns = [
    # path('', profile_view, name="v2_home"),

    path('categories', categories_view, name="v2_categories"),
    path('delete-category', delete_category, name="v2_delete_category"),
    path('edit-category', edit_category, name="v2_edit_category"),
    path('add-category', add_category, name="v2_add_category"),

    path('wallpapers', wallpapers_view, name="wallpapers"),
    path('add-wallpapers', add_wallpaper, name="add_wallpaper"),
    path('delete-wallpaper', delete_wallpaper, name="delete_wallpaper"),

    # path('settings', settings_view, name="v2_settings"),
    # path('delete-size', delete_size, name="v2_delete_size"),
]
