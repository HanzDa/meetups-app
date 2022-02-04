from django.contrib import admin
from .models import Locations, Meetup, Participant
# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date') # define how data will be shown in database
    # notice that their fields are the same as class attributes
    
    # also I can define filters
    list_filter = ('title', 'location', 'date')
    
    # add prepopulated fields to auto-generate a name
    prepopulated_fields = {'slug': ('title', )} 
    

admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Locations)
admin.site.register(Participant)
