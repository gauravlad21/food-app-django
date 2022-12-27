from django.urls import path
from .views import index, food_details

app_name = 'food'
urlpatterns = [
    path('food/', index, name='index'),
    path('food/<int:pk>/', food_details, name='detail'),
]
