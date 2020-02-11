from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .mock_lists import getMockResponse, getMockResponseRecipes
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db import IntegrityError
import requests


def create_user(request):
    email = request.GET.get('email', None)
    password = request.GET.get('password', None)

    try:
        user = User.objects.create_user(
            username=email,
            password=password,
            email=email
        )
    except ValueError as e:
        return JsonResponse({'error': 'Could not create user, invalid value: {}'.format(e)})
    except IntegrityError:
        return JsonResponse({'error': 'User already exists.'})

    try:
        user.save()
    except (Exception, IntegrityError) as e:
        return JsonResponse({'error': 'could not create user: {}'.format(e)})

    return JsonResponse({'success': True})



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

def make_recipe(request):
    token = request.GET.get('auth', None)
    weight = request.GET.get('weight', None)

    user = None
    if token is not None:
        user = Token.objects.get(key=token).user

    if user is not None and weight.isnumeric():
        user.profile.foodsaved = user.profile.foodsaved + int(weight)
        user.save()

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'User is not logged in/'})


def get_results(request):

    ingredients = request.GET.get('ingredients', None)
    token = request.GET.get('auth', None)
    if token is not None:
        user = Token.objects.get(key=token).user
        #do stuff with user preferences here

    #r = requests.get('https://api.edamam.com/search?q='+ ingredients +'&app_id=e4819de5&app_key=2092d79ab6d0992be43923df03bf42ed&from=0&to=3&calories=591-722&health=alcohol-free', params=request.GET)

    r = getMockResponseRecipes()
    json = r.json()

    #ordering function here

    if r.status_code == 200:
        return JsonResponse(json)
    else:
        return JsonResponse({'error': 'could not make request'})

