from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RecipeForm, RecipeImageForm
from .models import Profile, Recipe


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
    }
    return render(request, "./recipes/recipe_list.html", ctx)


@login_required
def recipe_create(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        form = RecipeForm(request.POST)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = profile
            recipe.save()

            return redirect(recipe.get_absolute_url())
    else:
        form = RecipeForm()

    ctx = {"form": form}
    return render(request, "./recipes/recipe_form.html", ctx)


@login_required
def recipe_add_image(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)

        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()

            return redirect(recipe.get_absolute_url())
    else:
        form = RecipeImageForm()

    ctx = {"form": form, "recipe": recipe}
    return render(request, "./recipes/recipe_image_form.html", ctx)


@login_required
def recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.all()
    images = recipe.image.all()

    ctx = {"recipe": recipe, "ingredients": ingredients, "images": images}

    return render(request, "./recipes/recipe.html", ctx)
