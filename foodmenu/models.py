from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Food(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=512)
    price = models.IntegerField()
    image = models.CharField(max_length=512,
                             default='https://png.pngtree.com/png-clipart/20190612/original/pngtree-black-and-'
                                     'white-variety-of-food-png-image_3319164.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('food:detail', kwargs={"pk": self.pk})
