from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/food_item_ac', views.food_item_ac, name='food_item_ac'),
]
