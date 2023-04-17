"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('recipes', views.RecipeViewSets)
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientviewSet)

app_name = 'recipe'

urlpatterns = [
     path('', include(router.urls))
]
