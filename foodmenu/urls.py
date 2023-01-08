from django.urls import path
from .views import FoodDetailsView, update_food, delete_food, IndexClassView, CreateFood

app_name = 'food'
urlpatterns = [
    path('food/', IndexClassView.as_view(), name='index'),
    path('food/<int:pk>/', FoodDetailsView.as_view(), name='detail'),
    path('food/add/', CreateFood.as_view(), name='add-food'),
    path('food/update/<int:pk>/', update_food, name='update-food'),
    path('food/update/<int:pk>/', delete_food, name='delete-food')
]
