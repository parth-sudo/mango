from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=10)
    about = models.TextField()

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    name = models.CharField(max_length=50)
    age = models.SmallIntegerField()
    bio = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name



