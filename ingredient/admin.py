from django.contrib import admin

# Register your models here.
from .models import ingredientItem, recipeItem

admin.site.register(ingredientItem)
admin.site.register(recipeItem)