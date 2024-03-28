from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cats/')
    rarity = models.CharField(max_length=20)
    description = models.TextField()