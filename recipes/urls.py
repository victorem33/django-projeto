from django.urls import path
from recipes.views import home
from . import views

#recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name = "home"),  # Home
    path('recipes/<int:id>/', views.recipe, name = "recipe"),
]