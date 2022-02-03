from django.db import models


class Locations(models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 300)
    
    def __str__(self):
        return f'{self.name} - {self.address}'


class Meetup(models.Model):
    title = models.CharField(max_length=255)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    img = models.ImageField(upload_to='images')
    
    def __str__(self):
        return f'{self.title} - { self.location }'
    
    
    
    
    