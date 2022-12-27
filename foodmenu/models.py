from django.db import models


class Food(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=512)
    price = models.IntegerField()

    def __str__(self):
        return self.title
