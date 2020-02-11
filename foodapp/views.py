from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .mock_lists import getMockResponse, getMockResponseRecipes, getOzBox, IngredientsList
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db import IntegrityError
from .models import Recipe, Profile
from .sorting import getOrderedRecipes, initialiseDic, leastNeededIngredient
from django.db.models import Avg
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

    ingredients = IngredientsList

    return JsonResponse({'data': ingredients})

def get_stats(request):
    token = request.GET.get('auth', None)

    if token is None:
        return JsonResponse({'error': 'token missing'})

    user = Token.objects.get(key=token).user

    if user is None:
        return JsonResponse({'error': 'user doesnt exist'})

    kgsaved = user.profile.foodsaved / 1000
    co2saved = 5 * kgsaved
    dollarsaved = 1.5 * kgsaved

    averagekgsaved = Profile.objects.all().aggregate(Avg('foodsaved'))
    averageco2saved = 5 * averagekgsaved
    averagedollarsaved = 1.5 * averagekgsaved

    stats = {
        'kgsaved': kgsaved,
        'co2saved': co2saved,
        'dollarsaved': dollarsaved,
        'avg_kgsaved': averagekgsaved,
        'avg_co2saved': averageco2saved,
        'avgdollarsaved': averagedollarsaved
    }

    return JsonResponse(stats)



def make_recipe(request):
    token = request.GET.get('auth', None)
    weight = request.GET.get('weight', None)
    id = request.GET.get('id', None)

    user = None
    if token is not None:
        user = Token.objects.get(key=token).user

    if user is not None and weight.isnumeric():
        user.profile.foodsaved = user.profile.foodsaved + int(weight)

        if id is not None:
            recipe = Recipe.objects.filter(apireference=id).first()
            print(recipe)
            if recipe is None:
                recipe = Recipe()
                recipe.apireference = id
                recipe.save()

            user.profile.cooked.add(recipe)

        user.save()

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'User is not logged in/'})


def get_results(request):


    ingredients = request.GET.get('q', None)
    preferences = request.GET.get('p', None)

    token = request.GET.get('auth', None)

    if token is not None:
        user = Token.objects.get(key=token).user
        #do stuff with user preferences here

    #r = requests.get('https://api.edamam.com/search?q='+ ingredients +'&app_id=e4819de5&app_key=2092d79ab6d0992be43923df03bf42ed&from=0&to=3&calories=591-722&health=alcohol-free', params=request.GET)

    r = getMockResponseRecipes()

    if r.status_code == 200:
        json = r.json()

        if ingredients is not None:
            if ingredients.find("OzBox ") !=-1:
                Inputs = getOzBox(ingredients)
            else:
                Inputs = ingredients.split(",")


            #adds matched ingredients from query string
            RecipeResult = json["hits"]
            for hits in RecipeResult:
                Recipe = hits["recipe"]
                Ingredients = Recipe["ingredientLines"]
                Match = []
                for I in Ingredients:
                    for i in Inputs:
                        I = I.lower()
                        i = i.lower()
                        if I.find(i) != -1:
                            Match.append(i.title())
                Recipe["match"] = Match

            json["hits"] = RecipeResult

            # orders list based on number of ingredients matched

            initialiseDic(json)
            leastNeededIngredient(Inputs, json)
            json = getOrderedRecipes(json)

            return JsonResponse(json, safe=False)
        else:
            return JsonResponse({'error': 'No ingredients'})
    else:
        return JsonResponse({'error': 'could not make request'})

