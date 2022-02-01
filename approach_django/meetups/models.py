from django.db import models

class Meetup(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    img = models.ImageField(upload_to='images')