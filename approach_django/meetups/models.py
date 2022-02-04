from django.db import models


class Participant(models.Model):
    email = models.EmailField(unique=True)
    
    def str(self):
        return self.email
        


class Locations(models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 300)
    
    def __str__(self):
        return f'{self.name} - {self.address}'


class Meetup(models.Model):
    title = models.CharField(max_length=255)
    organizer_email = models.EmailField(max_length=255)
    date = models.DateField(null=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    img = models.ImageField(upload_to='images')
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True)
    
    def __str__(self):
        return f'{self.title} - { self.location }'
    
    
    
    
    