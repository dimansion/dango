from django.db import models
from django.utils import timezone


class Portofolio(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField (upload_to="images/",null=True,blank=True)


    def __str__(self):
        return self.name
