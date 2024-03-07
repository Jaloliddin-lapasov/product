
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, blank=False)
    price = models.IntegerField(null=True, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} | {self.price}'

