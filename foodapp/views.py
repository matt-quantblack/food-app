from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .mock_lists import mock_food_list

def food_item_ac(request):

    word = request.GET.get('q', None)

    filtered = []

    if word is not None:
        for item in mock_food_list:
            if word.lower() in item.lower():
                filtered.append(item)

    return JsonResponse({'data': filtered})

def dashboard(request):
    return JsonResponse({'success': True})
