from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup
from .forms import RegistrationForm
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
    try:
        meetups_info = Meetup.objects.get(slug = meetup_slug)
        # render the article the first time
        if request.method == 'GET':
            registration_form = RegistrationForm()

            return render(request, 'meetups/more_details.html', {
                'meetups_info': meetups_info,
                'form': registration_form
                })
            
        # when input is post from the user
        else:
            registration_form = RegistrationForm(request.POST)
            
            if registration_form.is_valid():
                # save in database
                new_participant = registration_form.save()
                meetups_info.participants.add(new_participant)
                
    
        return render(request, 'meetups/more_details.html', {
            'meetups_info': meetups_info,
            'form': registration_form
            })
        
    except Exception as e:
        print(e)