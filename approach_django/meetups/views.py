from django.shortcuts import render
from django.http import HttpResponse
# in django a view is a simple python function

def index(request):
    # the path is relative to the templates folder
    
    # render could get a third argument and tha a dictionary or a json notation like this
    
    meetups_available = [
        {
            'title': 'this is the first meetup',
            'location': 'Chicago',
            'slug': 'first-meetup'
        },
        {
            'title': 'this is the second meetup',
            'location': 'Lodon',
            'slug': 'second-meetup'
        },
        {
            'title': 'this is the third meetup',
            'location': 'Montevideo',
            'slug': 'third-meetup'
        },
    ]
    
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups_available
    })


def more_details(request, meetup_slug):
    meetups_info = {
        'title': 'the first meetup',
        'description': 'this is a great meetup to learn about Django'
    }
    return render(request, 'meetups/more_details.html', {
        'meetups_info': meetups_info,
    })