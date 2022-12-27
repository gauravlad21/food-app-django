from .models import Food
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    food_items = Food.objects.all()
    context = {
        "food_items": food_items,
    }
    return render(request, 'foodmenu/index.html', context)


def food_details(request, pk):
    item = Food.objects.get(pk=pk)
    context = {
        "item": item,
    }
    return render(request, 'foodmenu/detail.html', context)
