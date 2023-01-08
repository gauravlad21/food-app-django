from .models import Food
from django.shortcuts import render, redirect
from .forms import FoodForm
from django.views.generic import ListView, DetailView, CreateView


def index(request):
    food_items = Food.objects.all()
    context = {
        "food_items": food_items,
    }
    return render(request, 'foodmenu/index.html', context)


class IndexClassView(ListView):
    model = Food
    template_name = 'foodmenu/index.html'
    context_object_name = 'food_items'


def food_details(request, pk):
    item = Food.objects.get(pk=pk)
    context = {
        "item": item,
    }
    return render(request, 'foodmenu/detail.html', context)


class FoodDetailsView(DetailView):
    model = Food
    template_name = 'foodmenu/detail.html'


def create_food(request):
    form = FoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request, 'foodmenu/food-form.html', {'form': form})


class CreateFood(CreateView):
    model = Food
    fields = ['title', 'desc', 'price', 'image']
    template_name = 'foodmenu/food-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


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
