from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .mock_lists import mock_food_list, mock_recipes, mock_ac, getMockResponse
import requests

def food_item_ac(request):

    word = request.GET.get('q', None)

    #r = requests.get('https://api.edamam.com/api/food-database/parser?ingr='+ word +'&app_id=fbd440e6&app_key=136f60c5db1a10c7dc8aab22aaccf545', params=request.GET)

    r = getMockResponse()
    json = r.json()
    if r.status_code == 200:
        ingredients = []
        print(json["parsed"])
        for i in json["parsed"]:
            ingredients.append(i["food"]["label"])
        for i in json["hints"]:
            ingredients.append(i["food"]["label"])
        return JsonResponse({'data': ingredients})
    else:
        return JsonResponse({'error': 'could not make request'})

def get_results(request):

    #ingredients = request.POST.getlist("ingredients[]")
    ingredients_string = request.GET('ingredients', None)
    if ingredients_string is not None:
        ingredients = ingredients_string.split(",")

    #select all recipes from api that have the listed ingredients
    #do some filtering
    #do some sorting
    recipes = mock_recipes

    return JsonResponse({'data': recipes})

def get_recipe(request):

    recipe_id = request.GET('id', None)

    #get the recipe from the api
    recipe = mock_recipes[0]

    return JsonResponse({'data': recipe})

def dashboard(request):
    return JsonResponse({'success': True})
