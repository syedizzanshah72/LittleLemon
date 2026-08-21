from django.db import models

# Create your models here.

class Menu(models.Model):
    dishname = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.dishname