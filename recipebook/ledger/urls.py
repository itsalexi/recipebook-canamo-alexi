from django.urls import path
from .views import recipe, recipe_add_image, recipe_create, recipe_list

urlpatterns = [
    path('recipes/list', recipe_list, name='recipe-list'),
    path('recipe/add', recipe_create, name='recipe-create'),
    path('recipe/<int:pk>/add_image', recipe_add_image, name='recipe-add-image'),
    path('recipe/<int:pk>', recipe, name='recipe'),
]

app_name = "ledger"
