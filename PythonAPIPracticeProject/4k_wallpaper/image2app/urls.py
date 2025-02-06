from django.urls import path 
from .views import add_category, categories_view, delete_category, edit_category, profile_view, settings_view, delete_size


urlpatterns = [
    path('', profile_view, name="v2_home"),

    path('categories', categories_view, name="v2_categories"),
    path('delete-category', delete_category, name="v2_delete_category"),
    path('edit-category', edit_category, name="v2_edit_category"),
    path('add-category', add_category, name="v2_add_category"),

    path('settings', settings_view, name="v2_settings"),
    path('delete-size', delete_size, name="v2_delete_size"),
]
