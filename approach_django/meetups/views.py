from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup, Participant
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
                # NOTE: in this case the save method doesn't really work for us since we want to let our participants to register in multiple meetups
                # so in this case we should use the cleaned_date attribute which is a dictionary
                # getting input from the user site
                user_email = registration_form.cleaned_data['email'] # pass the field we have define in our form
                
                new_participant, was_created = Participant.objects.get_or_create(email=user_email)
                print(was_created)
                meetups_info.participants.add(new_participant)
                
                return redirect('registration_success', meetup_slug=meetup_slug) # get name in url paths
                
    
        return render(request, 'meetups/more_details.html', {
            'meetups_info': meetups_info,
            'form': registration_form
            })
        
    except Exception as e:
        print(e)
        

def registration_success(request, meetup_slug):
    meetup_info = Meetup.objects.get(slug = meetup_slug)
    return render(request, 'meetups/registration-success.html', {
        'meetup_info': meetup_info
    })