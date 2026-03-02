from django.db import models
from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_bio = models.TextField(blank=True)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('ledger:ingredient', args=[str(self.name)])


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="recipe_author")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[str(self.name)])


class RecipeIngredient(models.Model):

    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return f"{self.ingredient} - {self.quantity}"
