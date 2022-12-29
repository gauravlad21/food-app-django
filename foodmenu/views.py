from .models import Food
from django.shortcuts import render, redirect
from .forms import FoodForm


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


def create_food(request):
    form = FoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request, 'foodmenu/food-form.html', {'form': form})


def update_food(request, pk):
    item = Food.objects.get(pk=pk)
    form = FoodForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'foodmenu/food-form.html', {'form': form})


def delete_food(request, pk):
    item = Food.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'foodmenu/food-delete.html', {'form': form})
