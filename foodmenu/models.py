from django.db import models


class Food(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=512)
    price = models.IntegerField()
    image = models.CharField(max_length=512,
                             default='https://png.pngtree.com/png-clipart/20190612/original/pngtree-black-and-'
                                     'white-variety-of-food-png-image_3319164.jpg')

    def __str__(self):
        return self.title
