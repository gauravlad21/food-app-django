from django.urls import path
from .views import index, food_details, create_food, update_food, delete_food

app_name = 'food'
urlpatterns = [
    path('food/', index, name='index'),
    path('food/<int:pk>/', food_details, name='detail'),
    path('food/add/', create_food, name='add-food'),
    path('food/update/<int:pk>/', update_food, name='update-food'),
    path('food/update/<int:pk>/', delete_food, name='delete-food')
]
