from django.shortcuts import render
from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
    }
    return render(request, "./recipes/recipe_list.html", ctx)


def recipe(request, name):
    recipe = Recipe.objects.get(name=name)
    ingredients = recipe.ingredients.all()
    ctx = {'name': str(recipe), 'ingredients': ingredients}
    return render(request, "./recipes/recipe.html", ctx)
