from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from django.contrib import admin

urlpatterns = [
    path('api/food_item_ac', views.food_item_ac, name='food_item_ac'),
    path('api/get_results', views.get_results, name='get_results'),
    path('api/get_substitutes', views.get_substitutes, name='get_substitutes'),
    path('api/make_recipe', views.make_recipe, name='make_recipe'),
    path('api/token-auth/', obtain_auth_token, name='token_auth'),
    path('api/create_user/', views.create_user, name='create_user'),
    path('api/get_stats/', views.get_stats, name='get_stats'),
    path('admin/', admin.site.urls),
]
