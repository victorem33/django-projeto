from django.urls import path
from recipes.views import home
from . import views

urlpatterns = [
    path('', views.home, name = 'recipe-home'),  # Home
    path('recipes/<int:id>/', views.recipe, name = 'recipe-recipe'),
]