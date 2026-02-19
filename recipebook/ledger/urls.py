from django.urls import path
from .views import recipe_list, recipe

urlpatterns = [
    path('recipes/list', recipe_list, name='recipe-list'),
    path('recipe/<str:name>', recipe, name='recipe'),
]

app_name = "ledger"
