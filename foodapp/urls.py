from django.urls import path

from . import views

urlpatterns = [
    path('api/food_item_ac', views.food_item_ac, name='food_item_ac'),
    path('api/get_results', views.get_results, name='get_resultspip '),
]
