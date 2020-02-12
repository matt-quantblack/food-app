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

    if word is None or word == "":
        ingredients = []
    else:
        ingredients = [i for i in IngredientsList if i.lower().startswith(word.lower())]

    return JsonResponse({'data': ingredients})

def get_stats(request):

    token = request.GET.get('auth', None)

    if token is None:
        return JsonResponse({'error': 'token missing'})

    user = Token.objects.get(key=token).user

    if user is None:
        return JsonResponse({'error': 'user doesnt exist'})

    history = []

    for item in user.profile.cooked.all():
        history.append({'id': item.apireference,
                       'name': item.name,
                        'imageurl': item.iurl,
                        'weight': item.weight})

    kgsaved = user.profile.foodsaved / 1000
    co2saved = user.profile.co2saved / 1000
    dollarsaved = user.profile.dollarsaved

    av = Profile.objects.all().aggregate(Avg('foodsaved'))
    averagekgsaved = av['foodsaved__avg'] / 1000
    averageco2saved = 5 * averagekgsaved
    averagedollarsaved = 1.5 * averagekgsaved

    badges = {'recycle': int(kgsaved / 5),
              'co2': int(co2saved / 15),
              'dollar': int(dollarsaved / 7.5)}
    nextkg = { 'value': ((float(kgsaved) / 5) - badges['recycle']) * 100, 'next': (badges['recycle']+1)}
    nextc02 =  {'value': ((float(co2saved) / 15) - badges['co2']) * 100, 'next':  (badges['co2']+1)}
    nextdollar = {'value': ((float(dollarsaved) / 7.5) - badges['dollar']) * 100, 'next':  (badges['dollar']+1)}

    next_badge = {'recycle': nextkg, 'co2': nextc02, 'dollar': nextdollar}



    stats = {
        'kgsaved': kgsaved,
        'co2saved': co2saved,
        'dollarsaved': dollarsaved,
        'avg_kgsaved': averagekgsaved,
        'avg_co2saved': averageco2saved,
        'avgdollarsaved': averagedollarsaved,
        'badges': badges,
        'next_badges': next_badge,
        'history': history
    }

    return JsonResponse(stats)



def make_recipe(request):
    token = request.GET.get('auth', None)
    weight = request.GET.get('weight', None)
    id = request.GET.get('id', None)
    name = request.GET.get('name', None)
    imageurl = request.GET.get('imageurl', None)



    user = None
    if token is not None:
        user = Token.objects.get(key=token).user

    try:
        weight = float(weight)
        weight = int(weight)
    except ValueError:
        return JsonResponse({'error': 'Weight not a valid number'})

    co2 = weight * 5
    dollar = weight * 1.5 / 1000

    if user is not None:
        user.profile.foodsaved = user.profile.foodsaved + int(weight)
        user.profile.co2saved = user.profile.co2saved + int(co2)
        user.profile.dollarsaved = user.profile.dollarsaved + int(dollar)

        if id is not None:
            recipe = Recipe.objects.filter(apireference=id).first()

            if recipe is None:
                recipe = Recipe()
                recipe.apireference = id
                recipe.name = name
                recipe.iurl = imageurl
                recipe.weight = int(weight)
                recipe.save()

            user.profile.cooked.add(recipe)

        user.save()

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'User is not logged in/'})

def get_results(request):

    ingredients = request.GET.get('q', None)
    preferences = request.GET.get('p', "")
    if preferences != "":
        preferences = preferences.replace(",","&health=")
        preferences = "&health=" + preferences

    token = request.GET.get('auth', None)
    uri = 'https://api.edamam.com/search?q='+ ingredients +'&app_id=e4819de5&app_key=2092d79ab6d0992be43923df03bf42ed&from=0&to=100'+preferences

    if token is not None:
        try:
            user = Token.objects.get(key=token).user
        except:
            print("No user")
        #do stuff with user preferences here

    #r = requests.get(uri, params=request.GET)

    r = getMockResponseRecipes()

    if r.status_code == 200:
        json = r.json()

        if ingredients is not None:
            if ingredients.lower().find("ozbox ") !=-1:
                Inputs = getOzBox(ingredients)
            else:
                Inputs = ingredients.split(",")

            print(Inputs)

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
                Recipe["match"] = list(set(Match))
                Recipe["method"] = ["1. Preheat oven to 200°c. Combine ricotta, grated parmesan, egg, finely grated lemon rind, thyme leaves and pinch dried chilli flakes in a bowl. Season.",
                                    "2. Spoon into 4 x 10cm heart-shaped pans. Brush tops with olive oil. Bake for 20 minutes or until golden and set.",
                                    "3. Serve with toast and tomato medley and basil."]

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

