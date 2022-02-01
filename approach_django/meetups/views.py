from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup
# in django a view is a simple python function

def index(request):
    # the path is relative to the templates folder
    
    # render could get a third argument and tha a dictionary or a json notation like this
    
    meetups_available = Meetup.objects.all()
    
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups_available
    })


def more_details(request, meetup_slug):
    meetups_info = Meetup.objects.get(slug = meetup_slug)
    return render(request, 'meetups/more_details.html', {
        'meetups_info': meetups_info,
    })